# ⚡ KinSync — AI-Powered Family Logistics & Calendar Command Hub

**KinSync** is a modern, glassmorphic executive command platform designed for multi-child family scheduling, driver assignments, packing lists, live Google Maps directions, and AI logistics coordination.

Built with **Google Agent Development Kit (ADK)**, **Vertex AI Reasoning Engine**, and **A2UI v0.8**.

---

## 🌟 Key Features

- 📊 **Executive Daily Briefs**: Automated morning breakdown of drop-offs, pickups, estimated drive times, and daily family routines.
- 📅 **Compact Activity Pill Grid**: Responsive grid displaying family member color tags, time badges, category labels, location details, and packing checklists.
- 🚗 **Driver Assignments & Logistics**: Track drop-off and pickup drivers (`Dad (Mark)`, `Mom (Sarah)`, `Grandma Helen`) for every event.
- 🗺️ **Live Google Maps & Travel Times**: One-click Google Maps directions (`Origin: Home Base` $\rightarrow$ `Destination`) with estimated drive time badges (e.g. `🚗 ~12 mins (3.4 mi) from Home`).
- ✏️ **Interactive Activity Editing**: Edit or delete activities directly from any card with live UI re-rendering and automatic AI state synchronization.
- 👥 **Family Roster & Member Profiles**: Track roles, birthdays, vehicle details, driver preferences, and routine notes.
- ✨ **KinSync AI Assistant Drawer**: Floating assistant drawer powered by Vertex AI Reasoning Engine & A2UI v0.8 for conversational schedule queries, conflict detection, and briefs.

---

## 🏗️ Architecture & Tech Stack

```
   ┌───────────────────────┐          ┌─────────────────────────┐          ┌─────────────────────────────┐
   │                       │          │  FastAPI Proxy Server   │   A2A    │   Vertex AI ReasoningEngine │
   │  Glassmorphic Web App │ ───────> │    (kinsync/frontend)   │ ───────> │       (Google ADK Agent)    │
   │  (HTML5 / CSS / JS)   │  HTTP    │    Port: 8080           │ Protocol │   `gemini-2.5-flash` + A2UI │
   └───────────────────────┘          └─────────────────────────┘          └─────────────────────────────┘
```

- **Core Agent**: Built with [Google ADK](https://github.com/google/adk) using `gemini-2.5-flash`.
- **A2UI Integration**: Uses `A2uiSchemaManager` (version `0.8`) with `BasicCatalog` and `a2ui_callback`.
- **Frontend App**: FastAPI server serving a single-page web app styled with glassmorphism, `Plus Jakarta Sans` body typography, `Outfit` bold headers, and Material Symbols icons.
- **Location Base**: Configured home base (`742 Evergreen Terrace, Palo Alto, CA 94301`) for Google Maps route calculation.

---

## 📁 Project Structure

```
kinsync/
├── app/                        # Core agent implementation
│   ├── agent.py                # Main ADK agent definition & A2UI schema manager
│   ├── tools.py                # Schedule tools, conflict detection & in-memory storage
│   └── a2ui_utils.py           # A2UI model callback renderer
├── frontend/                   # Web frontend & FastAPI proxy
│   ├── main.py                 # FastAPI server proxying requests to Agent Engine over A2A
│   └── static/
│       ├── index.html          # Glassmorphic web app UI with Maps & Edit modals
│       └── kinsync_ai_avatar.png # AI Assistant avatar
├── deployment/                 # Deployment scripts & build metadata
├── pyproject.toml              # Dependencies (google-adk, google-genai, fastapi, uvicorn)
├── agents-cli-manifest.yaml    # Agents CLI deployment manifest
└── README.md                   # Project documentation
```

---

## 🚀 Quick Start & Local Execution

### 1. Requirements
- **Python**: `>=3.11`
- **uv**: Package manager ([Install Guide](https://docs.astral.sh/uv/))

### 2. Environment Variables
Set your deployed Reasoning Engine resource name:

```bash
export AGENT_ENGINE_RESOURCE_NAME="projects/68219776871/locations/us-east1/reasoningEngines/8436033750436937728"
export AGENT_DIRECTORY="app"
```

### 3. Run the Server
Launch the FastAPI frontend proxy server:

```bash
uv run python main.py
```

Open your browser at `http://localhost:8080` to access the KinSync platform.

---

## 🛠️ Commands Reference

| Command | Description |
| ------- | ----------- |
| `uv run python main.py` | Run the local FastAPI proxy server & Web UI on port 8080 |
| `agents-cli playground` | Launch local development agent playground |
| `agents-cli deploy` | Deploy agent to Vertex AI Reasoning Engine |
| `uv run pytest tests/` | Run unit and integration tests |

---

## 🎨 UI Highlights

- **Executive Brief**: Morning briefing hero banner with schedule health indicators and detailed drop-off/pickup timelines.
- **Family Roster**: Visual member profile cards with custom color avatars and routine notes.
- **Activity Pills**: Grid layout displaying date/time, category tags, driver pills, drive time badges, and Google Maps links.
- **Interactive Editing**: Glassmorphic modal form to edit activity title, dates, times, drivers, venue address, and packing notes.
