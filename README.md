# FastAPI MongoDB Backend

This is a **FastAPI** backend application for managing student data, using **MongoDB** as the database. The project demonstrates CRUD operations, proper data validation with Pydantic, and asynchronous database handling with **Motor**.

---

## Features

- **Add Student** – Add a new student to the database.
- **Retrieve Students** – Get all students or a specific student by ID.
- **Update Student** – Update student data (any field).
- **Delete Student** – Delete a student by ID.
- **Asynchronous Operations** – Powered by Motor for async MongoDB queries.
- **Data Validation** – Using Pydantic models (`StudentSchema` and `StudentModel`).

---

## Tech Stack

- **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** [MongoDB Atlas / Compass](https://www.mongodb.com/)
- **MongoDB Driver:** [Motor](https://motor.readthedocs.io/en/stable/)
- **Python Version:** 3.10+
- **Environment Management:** `venv` and `.env` for secrets

---

## Folder Structure

