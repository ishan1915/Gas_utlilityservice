# Gas_utlilityservice
# 🚀 Gas Utility Service Request System

A Django-based application to manage service requests for a gas utility company. This system allows customers to submit service requests, track their status, and view account information. It also provides an admin dashboard for customer support representatives to manage requests.

---

## 🌟 Features

✅ **User Authentication** (JWT-based login & registration)  
✅ **Service Requests** (Customers can submit requests online)  
✅ **Request Tracking** (Monitor request status updates)  
✅ **Admin Dashboard** (Support reps can manage requests)  
✅ **File Attachments** (Customers can upload relevant files)  
✅ **REST API** (Built using Django REST Framework)  
✅ **Modular Codebase** (Follows best Django practices)  

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/gas-utility-service.git
cd gas-utility-service
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables
Create a `.env` file in the project root and add:
```env
SECRET_KEY=your-secret-key
DEBUG=True
```

### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations users service_requests
python manage.py migrate
```

### 5️⃣ Create a Superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```
Access the API at `http://127.0.0.1:8000/`

---

## 🚀 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST   | `/api/auth/register/` | Register a new user |
| POST   | `/api/auth/token/` | Obtain JWT token |
| GET    | `/api/requests/` | List all service requests |
| POST   | `/api/requests/` | Create a new request |
| PATCH  | `/api/requests/<id>/` | Update request status |
| DELETE | `/api/requests/<id>/` | Delete a request |

---

## 🏗️ Project Structure
```
├── config/               # Django project settings
├── users/                # User authentication module
├── service_requests/     # Service request management
├── media/                # Uploaded media files
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
```

---

## 📸 Admin Panel
Run the server and visit `http://127.0.0.1:8000/admin/` to access the admin dashboard.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contribution
Feel free to submit pull requests or report issues to improve this project!

🚀 Happy Coding! 🚀

