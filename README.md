## IPLAuction

IPLAuction is a small Python project that mimics the IPL auction process using a Tkinter GUI.

It was built as a course project at PES University and allows you to:

- Load players with stats from a CSV file
- Run an auction with 10 IPL teams
- Bid on players, sell them to teams, and
- Track remaining team wallets live in the interface

---

## Requirements

- Python 3.10+ (with Tk / tkinter support)
- pip (Python package manager)

Python standard library modules used:

- tkinter (GUI)
- csv, os (file and path handling)

Third‑party package (installed via pip):

- Pillow (PIL)

Install dependencies with:

```bash
pip install -r requirements.txt
```

> Note: On macOS and some Linux distros you may need to ensure Tk is installed (e.g. via the official Python.org installer or your package manager) so `tkinter` works.

---

## Project Structure

- `main.py` – core logic, player loader and image helper
- `interface.py` – Tkinter GUI; drives the auction
- `data.py` – CSV read/write helpers and team wallet calculations
- `data/playerdata/player_data.csv` – player database (CSV)
- `data/playerdata/enterplayerdata.py` – helper script to enter players interactively
- `data/auction_files/team_data.csv` – output of sold players per team
- `pics/public/` – general UI images (logo, auction image, etc.)
- `pics/playerpics/` – individual player photos
- `pics/teampics/` – team logos

---

## Setup

1. **Clone the repository**

	```bash
	git clone <repo-url>
	cd IPLAuction
	```

2. **Create and activate a virtual environment (recommended)**

	```bash
	python3 -m venv .venv
	source .venv/bin/activate  # macOS / Linux
	# .venv\Scripts\activate  # Windows (PowerShell / CMD)
	```

3. **Install dependencies**

	```bash
	pip install -r requirements.txt
	```

Make sure Python can import `tkinter`. If `import tkinter` fails, install Tk for your OS (Python.org installer on Windows/macOS usually includes it; on Linux use your distro’s package manager).

---

## Adding Players

Players are stored in `data/playerdata/player_data.csv`. You can populate this file using the helper script:

```bash
python3 data/playerdata/enterplayerdata.py
```

The script prompts for a list of values for each field. The columns are:

1. `type` – player role (`batsman`, `bowler`, `allrounder`, `keeper`)
2. `pic` – relative path to the player image (e.g. `pics/playerpics/abd.jpeg`)
3. `name`
4. `age`
5. `country`
6. `spec` – specialization / description
7. `exp` – experience (years)
8. `matches`
9. `runs`
10. `wickets`
11. `catches`
12. `stumpings`
13. `base` – base price in crores
14. `bid` – starting bid (usually `0`)

Enter all values for one field, then type `q` to move to the next field.

Example `pic` values must match real files under `pics/playerpics/`.

---

## Running the Auction

From the project root with your virtual environment active:

```bash
python3 main.py
```

This imports the data and launches the Tkinter interface (via `interface.py`). You can also run the GUI directly:

```bash
python3 interface.py
```

### Interface Overview

The main window shows:

- Player photo and stats
- Base price and current bid
- Ten team buttons with logos and current wallet (starting at 100 cr)
- Current highest bid and team logo
- `Next Player` and `sold` buttons

### Basic Flow

1. Click **Next Player** to bring a new player to the auction.
2. Click a **team logo** to place/increase a bid for that team.
3. The **current bid** and **current bidding team** update live.
4. Click **sold** to sell the player to the current highest bidder:
	- A record is appended to `data/auction_files/team_data.csv`.
	- The buying team’s wallet is reduced and updated in the UI.
5. Repeat for all players. When the generator runs out of players, the interface shows **“Auction over”** and disables further bidding.

---

## Data Files

- **Player data** – `data/playerdata/player_data.csv`
  - Read at startup to build the auction roster.
  - Image paths can use either `\` or `/`; paths are normalized internally.

- **Team data** – `data/auction_files/team_data.csv`
  - Each sold player is appended as a row: `[team, player_name, price]`.
  - `team_wallet(team)` recomputes the remaining wallet from this file (starting at 100 cr per team).

---

## Notes

- The project currently uses simple CSV files for persistence.
- Tkinter layouts are pixel‑based and tuned for a 600x600 window.
- If you change image filenames or add teams/players, ensure paths in the CSV and the `pics/` folders stay in sync.

Feel free to extend the project with features like team views, filters by player type, or exporting auction results.