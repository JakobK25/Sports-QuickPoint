# Sports-QuickPoint

A simple sports scoring system that tracks goals across multiple teams and provides statistical analysis.

## Features

- Real-time score tracking for multiple teams
- Database storage of scoring events with timestamps
- Statistical analysis of team performance
- Random score generation for testing and demonstration

## Tech Stack

- Python
- PostgreSQL database
- Docker for containerization
- pygame and pyFirmata for potential hardware integration

## Setup

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- PostgreSQL client (optional, for direct database access)

### Environment Variables

Copy `.env.example` to `.env` and fill in the required variables:

```
POSTGRES_PASSWORD=your_password
POSTGRES_DB=scoredb
```

### Database Setup

#### Using Docker Compose (Recommended)

```sh
# Start the PostgreSQL container
docker compose up -d
```

#### Manual Docker Setup

```sh
# Build the image
docker build -t sports-quickpoint-db .

# Run the container
docker run --name sports-db -d -p 5432:5432 --env-file .env sports-quickpoint-db
```

### Application Setup

```sh
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Database Schema

The application uses a simple schema with a `scores` table:

```sql
CREATE TABLE scores (
    scores_time TIMESTAMP,
    scores_team_name VARCHAR(100) NOT NULL,
    scores_goals VARCHAR(255)
);
```

## Usage

When running the application:
1. The system connects to the PostgreSQL database
2. It generates random scores for teams (HOLD1, HOLD2, HOLD3, HOLD4)
3. Scores are stored in the database with timestamps
4. Basic statistics are displayed in the console

## License

This project is licensed under CC0 1.0 Universal - see the [LICENSE](LICENSE) file for details.
