# Football Data Aggregator ⚽️

A Python-based backend that fetches football data from **API-Football** for LAFC (MLS) using **GitHub Actions**, and serves it as static JSON files. Ideally suited for SwiftUI MVVM applications to consume directly via GitHub Raw or Pages.

## 🎯 Goal
- **Source**: API-Football (RapidAPI)
- **Target**: Static JSON files hosted on GitHub
- **Limit**: Strictly under 100 requests/day
- **Consumer**: Mobile apps (SwiftUI) replacing API Base URL with GitHub URL.

## 🏗 Architecture (MVVM)

This project follows a clean **MVVM (Model-View-ViewModel)** architecture adapted for data fetching:

| Layer | Responsibility | Path |
|-------|----------------|------|
| **Models** | Data structures (Pydantic) defining the schema. | `app/models/` |
| **Services** | Raw API wrappers. One Service per Endpoint. Clean interactions. | `app/services/` |
| **ViewModels** | Business logic, rate limiting decision, orchestrating updates. | `app/viewmodels/` |
| **Storage** | Saves JSON to disk only if data changed to minimize commits. | `app/storage/` |
| **Scripts** | Entry points for GitHub Actions to trigger ViewModels. | `scripts/` |

## ⏱️ API Budget Strategy

Strict adherence to **100 requests/day**.

| Workflow | Frequency | Est. Calls | Strategy |
|----------|-----------|------------|----------|
| **Daily** | Every 6 hours | ~8 / day | Fetches Fixtures List + Standings. |
| **Live (Paused)** | Every 5 mins (Match only) | ~50 / match | Checks local index. if Live, fetches Events/Stats. Stops if finished. |
| **Seasonal**| Manual | ~2 / run | Fetches Players (Squad) & Team Info. |
| **Annual** | Manual | ~1 / run | Fetches Venues. |

**Protection Logic:**
- `LiveViewModel` checks locally cached schedule before calling API.
- If a match is detected "Live", it fetches `events` (critical) mostly, and `stats` occasionally.
- `JsonStore` prevents Git commits if data is identical to previous run.

## 📱 Using with SwiftUI App

This project is designed to be a **drop-in specific replacement** for API-Football in your Swift app.

**1. Change Base URL**
In your Swift API Client, simply swap the `baseURL`:

```swift
// Old
static let baseURL = "https://v3.football.api-sports.io"

// New (GitHub Raw)
static let baseURL = "https://raw.githubusercontent.com/<YOUR_USERNAME>/football-data/main/data"
```

**2. Endpoint Compatibility**
No other code changes required. The file structure mirrors the API endpoints:

| API Point | GitHub Path |
|-----------|-------------|
| `/fixtures` | `/fixtures/index.json` |
| `/fixtures/events?fixture=ID` | `/fixtures/events/ID.json` |
| `/standings` | `/standings/index.json` |
| `/players` | `/players/2025.json` |

## ⚙️ GitHub Actions

- **`daily.yml`**: Runs `scripts/fetch_daily.py`. Updates Fixtures List & Standings.
- **`live.yml`**: Runs `scripts/fetch_live.py`. Checks for active match. If active, updates score/events every 5 mins.
- **`seasonal.yml`**: Runs `scripts/fetch_seasonal.py`. Updates Rosters/Team Data.
- **`annual.yml`**: Runs `scripts/fetch_annual.py`. Updates Venues.

## 🚀 Setup Instructions

1. **Clone Repo**
   ```bash
   git clone https://github.com/your/football-data.git
   cd football-data
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   Copy `.env.example` to `.env` and add your API Key:
   ```bash
   cp .env.example .env
   ```
   *Edit `.env` with your `FOOTBALL_API_KEY`.*

4. **Run Locally**
   ```bash
   python scripts/fetch_daily.py
   ```

## 🔧 Environment Variables

Set these in **GitHub Repository Secrets** for Actions to work:

- `FOOTBALL_API_KEY`: Your RapidAPI Key.

Optional Variables (Vars):
- `TEAM_ID`: Default `1616` (LAFC).
- `LEAGUE_ID`: Default `253` (MLS).

## 📦 Deployment

1. Push this code to GitHub.
2. Go to **Settings > Secrets and variables > Actions**.
3. Add `FOOTBALL_API_KEY`.
4. Enable Actions if disabled.
5. Manually trigger `daily` workflow to seed data.

## 📈 Scaling
To add more teams or leagues:
1. Update `TEAM_ID` / `LEAGUE_ID` in `.env` or Action Variables.
2. Or modify `settings.py` to iterate over a list of teams (Caution: API Limits apply per request).
