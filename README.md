# The Cover — Sports Betting Signals & Narrative Insights (Preview)

**The Cover** is a data-driven insights app for bettors. Think **Bloomberg for betting**:
- Real-time **odds & line movement** signals
- **AI-style projections** and expected value (EV) summaries
- Clear, human **narratives** that explain the numbers

> This repository is a *public preview* of our direction. It includes:
> - A mock API (OpenAPI spec + example responses)
> - Static UI mockups
> - Product vision, compliance stance, and roadmap
> - No production systems, no sportsbook functionality

**We are not a sportsbook.** We do not take bets. This project provides information only.

## Quick start (mock API)
```bash
# Optional: run a tiny mock server (requires Python 3.10+)
pip install fastapi uvicorn
python src/app.py
# Visit http://localhost:8000/docs for live mock endpoints
```

What’s here
• api/openapi.yaml — documented endpoints for odds, projections, line moves (mocked)
• api/mock/*.json — example responses
• docs/ — vision, UX wireframes, compliance, data sourcing
• src/sample_frontend/ — static HTML/CSS mock UI (no framework)
• ROADMAP.md — phases, milestones, and integration plan

Ethics & Compliance
• We geofence for legal jurisdictions only (planned).
• We provide information, not wagering.
• We include tools for limits, self-exclusion links, and responsible gaming resources.

Contact: team@thecover.app

---