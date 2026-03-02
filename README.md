# Remote Farm Management System

A comprehensive IoT and AI-powered platform for remote farm monitoring and management, enabling farmers to oversee crop, livestock, and worker activities from anywhere.

## Overview

This system integrates:
- **Real-time Monitoring**: IoT sensors and CCTV feeds for continuous farm oversight
- **AI/ML Analytics**: PyTorch-based models for disease detection and predictive analytics
- **Web Dashboard**: React-based user interface for data visualization
- **REST APIs**: Django/FastAPI backend for seamless data flow
- **Cloud Infrastructure**: Docker containerization and Kubernetes orchestration
- **Mobile App**: React Native mobile application for on-the-go access

## Technology Stack

### Frontend
- React.js with Redux for state management
- Tailwind CSS for styling
- Chart.js/Recharts for data visualization
- React Router for navigation

### Backend
- Django REST Framework for API development
- FastAPI for async operations
- PostgreSQL for data persistence
- RabbitMQ for message queuing

### AI/ML
- PyTorch for deep learning models
- CNN for image analysis and disease detection
- OpenCV for video processing
- TensorFlow for prediction models

### DevOps & Infrastructure
- Docker & Docker Compose
- Kubernetes for orchestration
- GitHub Actions for CI/CD
- AWS/Azure cloud hosting

## Project Structure

```
remote-farm-management-system/
├── backend/                 # Django & FastAPI backend
├── frontend/                # React frontend application
├── ml_models/               # PyTorch ML models
├── mobile/                  # React Native mobile app
├── config/                  # Configuration files
├── database/                # Database schemas and migrations
├── tests/                   # Test suites
├── .github/                 # GitHub Actions workflows
├── docker-compose.yml       # Multi-container setup
└── docs/                    # Project documentation
```

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.9+
- Node.js 16+
- PostgreSQL 13+

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/remote-farm-management-system.git
cd remote-farm-management-system
```

2. **Setup with Docker Compose**
```bash
docker-compose up -d
```

3. **Initialize database**
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```

4. **Access the application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

## Features

### Dashboard Features
- Real-time crop monitoring
- Livestock health tracking
- Worker activity logs
- Environmental conditions (temperature, humidity, soil moisture)
- Disease detection alerts
- Resource usage analytics
- Financial tracking (profit/loss analysis)

### AI Capabilities
- Crop disease detection via CNN
- Predictive analytics for yield forecasting
- Anomaly detection in farm operations
- Resource optimization recommendations

### Mobile Features
- Real-time notifications
- CCTV feed streaming
- Daily activity logging
- Offline data sync
- Push alerts for critical events

## API Documentation

API endpoints are documented in `/docs/API_DOCUMENTATION.md`

Key endpoints:
- `GET /api/farms/` - List all farms
- `GET /api/crops/` - Crop data
- `GET /api/livestock/` - Livestock data
- `POST /api/alerts/` - Create alerts
- `GET /api/analytics/` - Analytics data

## Database Schema

See `database/schema.sql` for complete database structure

Main tables:
- Users & Roles
- Farms & Fields
- Crops & Growth Stages
- Livestock & Health Records
- Sensors & IoT Devices
- CCTV Cameras & Feeds
- Alerts & Notifications
- Financial Records

## Deployment

### Local Development
```bash
docker-compose up -d
```

### Production Deployment
See `docs/DEPLOYMENT.md` for cloud deployment guides (AWS, Azure, GCP)

## Testing

Run tests with:
```bash
# Backend tests
docker-compose exec backend pytest

# Frontend tests
docker-compose exec frontend npm test

# ML model tests
python tests/test_ml_models.py
```

## Configuration

Environment variables are managed in `.env` files:
- `backend/.env` - Django settings
- `frontend/.env` - React configuration
- `ml_models/.env` - ML model settings

See `config/example.env` for template

## CI/CD Pipeline

GitHub Actions workflow automates:
- Automated testing on pull requests
- Code quality checks
- Docker image building
- Automated deployment to staging/production

See `.github/workflows/` for pipeline configuration

## Security

- JWT-based authentication
- Role-based access control (RBAC)
- Data encryption at rest and in transit
- SQL injection prevention
- CSRF protection
- Input validation

## Contributing

1. Create a feature branch
2. Make your changes
3. Write/update tests
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support & Documentation

- User Guide: `/docs/USER_GUIDE.md`
- Installation Guide: `/docs/INSTALLATION.md`
- API Documentation: `/docs/API_DOCUMENTATION.md`
- Deployment Guide: `/docs/DEPLOYMENT.md`

## Contact

For support, email: support@remotefarm.com

## Acknowledgments

Built based on the research proposal: Remote Farm Management System

Last Updated: 2025
