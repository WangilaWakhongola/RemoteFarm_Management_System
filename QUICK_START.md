# Quick Start Guide

Get the Remote Farm Management System up and running in 5 minutes!

## 1. Prerequisites Check

```bash
# Check Docker
docker --version  # Should be 20.10+

# Check Docker Compose
docker-compose --version  # Should be 1.29+

# Check Git
git --version  # Should be 2.25+
```

## 2. Clone & Setup

```bash
# Navigate to project directory
cd remote-farm-management-system

# Copy environment variables
cp .env.example .env

# Edit .env if needed (optional for quick start)
# nano .env
```

## 3. Start Everything

```bash
# Build and start all services
docker-compose up -d

# Wait for services to be ready (30-60 seconds)
docker-compose ps
```

## 4. Initialize Database

```bash
# Run migrations
docker-compose exec backend python manage.py migrate

# Create admin user (follow prompts)
docker-compose exec backend python manage.py createsuperuser
```

## 5. Access Applications

Open these URLs in your browser:

- **Frontend**: http://localhost:3000
- **Admin Panel**: http://localhost:8000/admin
- **API**: http://localhost:8000/api/

## Useful Commands

### View Logs
```bash
# Backend logs
docker-compose logs -f backend

# Frontend logs
docker-compose logs -f frontend

# All logs
docker-compose logs -f
```

### Run Django Commands
```bash
# Create superuser
docker-compose exec backend python manage.py createsuperuser

# Load sample data
docker-compose exec backend python manage.py loaddata sample_data.json

# Run migrations
docker-compose exec backend python manage.py migrate
```

### Database Management
```bash
# Access PostgreSQL
docker-compose exec postgres psql -U postgres -d farm_management

# Backup database
docker-compose exec postgres pg_dump -U postgres farm_management > backup.sql

# Restore database
docker-compose exec -T postgres psql -U postgres farm_management < backup.sql
```

### Stop Services
```bash
# Stop without removing volumes
docker-compose stop

# Stop and remove everything
docker-compose down

# Stop and remove with volumes (WARNING: deletes data!)
docker-compose down -v
```

## API Testing

### Using cURL
```bash
# Get authentication token
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password"}'

# Get farms (replace TOKEN)
curl -H "Authorization: Bearer TOKEN" \
  http://localhost:8000/api/farms/
```

### Using Python
```python
import requests

# Login
response = requests.post(
    'http://localhost:8000/api/token/',
    json={'username': 'admin', 'password': 'password'}
)
token = response.json()['access']

# Get farms
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('http://localhost:8000/api/farms/', headers=headers)
print(response.json())
```

## Common Issues

### Port Already in Use
```bash
# Find what's using port 8000
lsof -i :8000

# Use different port (edit docker-compose.yml)
# Or stop other services
```

### Database Won't Start
```bash
# Check database logs
docker-compose logs postgres

# Reset database
docker-compose down -v
docker-compose up -d postgres
docker-compose exec postgres pg_isready
```

### Permission Denied
```bash
# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

### Out of Memory
```bash
# Stop some services
docker-compose stop celery_worker celery_beat

# Or increase Docker memory limit (Docker Desktop settings)
```

## Project Structure

```
remote-farm-management-system/
├── backend/          # Django REST API
├── frontend/         # React web app
├── ml_models/        # PyTorch models
├── mobile/           # React Native app
├── docs/             # Documentation
├── config/           # Configuration files
├── database/         # Database schemas
└── docker-compose.yml
```

## Next Steps

1. **Read Full Documentation**
   - See `docs/INSTALLATION.md` for detailed setup
   - See `docs/API_DOCUMENTATION.md` for API details

2. **Create Your First Farm**
   - Go to http://localhost:3000
   - Login with admin credentials
   - Add a farm through the UI or API

3. **Add Sample Data**
   - Create crops, fields, livestock
   - Set up sensors
   - Configure alerts

4. **Explore ML Features**
   - Upload crop images for disease detection
   - Get yield predictions
   - View analytics

5. **Customize for Your Needs**
   - Modify models in backend/apps/
   - Update React components in frontend/src/
   - Train ML models with your data

## File Locations

| What | Where |
|------|-------|
| Backend code | `backend/apps/` |
| Frontend code | `frontend/src/` |
| ML models | `ml_models/` |
| Configuration | `.env`, `config/nginx.conf` |
| Database | PostgreSQL (port 5432) |
| Cache | Redis (port 6379) |
| Queue | RabbitMQ (port 5672) |

## Important Notes

⚠️ **Development Only**
- This setup is for development/testing
- Change SECRET_KEY before production
- Configure proper SSL certificates
- Update ALLOWED_HOSTS for your domain

✅ **Production Ready**
- See `docs/DEPLOYMENT.md` for production setup
- Use Docker Compose to run locally
- Use Kubernetes for production scaling

## Getting Help

- **API Issues**: Check `docs/API_DOCUMENTATION.md`
- **Installation Issues**: See `docs/INSTALLATION.md`
- **Database Issues**: Check `database/init.sql`
- **ML Issues**: See `ml_models/README.md`

## Monitoring

### Health Checks
```bash
# Check all services
curl http://localhost:8000/api/health/

# Check specific service
curl http://localhost:3000/health
```

### Resource Usage
```bash
# View container stats
docker stats

# View specific container
docker stats container_name
```

## Development Mode

### Backend Development
```bash
# If you want to develop locally without Docker
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

### Frontend Development
```bash
# If you want to develop locally without Docker
cd frontend
npm install
npm start
```

## Tips & Tricks

1. **Speed up migrations**: `docker-compose exec backend python manage.py migrate --plan`
2. **Clean up Docker**: `docker system prune -a`
3. **View database**: Use pgAdmin at `http://localhost:5050` (configure in docker-compose.yml)
4. **Scale workers**: `docker-compose up -d --scale celery_worker=3`
5. **Monitor queue**: Use Flower (Celery monitoring tool)

## Troubleshooting Checklist

- [ ] Docker is running
- [ ] Ports 3000, 8000, 5432 are free
- [ ] .env file is created
- [ ] Migrations ran successfully
- [ ] Superuser was created
- [ ] No errors in docker logs

## Success Indicators

You'll know everything is working when:
- ✅ `docker-compose ps` shows all services running
- ✅ http://localhost:3000 loads the frontend
- ✅ http://localhost:8000/admin is accessible
- ✅ API token endpoint returns a token
- ✅ Database queries work

---

**Stuck?** Check the full documentation or run:
```bash
docker-compose logs -f
```

Happy farming! 🌾
