# PsyPredict - Mental Health Prediction System

A machine learning system for predicting mental health treatment needs based on survey data. This project provides data preprocessing, model training, and deployment capabilities through multiple interfaces.

## 🚀 Features

- **Data Preprocessing**: Automated cleaning and encoding of mental health survey data
- **Model Training**: Random Forest and Logistic Regression models with hyperparameter tuning
- **Model Explainability**: SHAP-based feature importance analysis
- **Multiple Interfaces**:
  - Streamlit web app for interactive predictions
  - FastAPI REST API for programmatic access
  - Jupyter notebooks for data exploration and development
- **Docker Support**: Containerized deployment with Docker Compose

## 📁 Project Structure

```
PsyPredict/
├── api/
│   └── app.py                 # FastAPI REST API
├── dashboard/
│   └── dashboard.py           # Dashboard interface
├── notebooks/
│   ├── eda_mental_health.ipynb                    # Exploratory Data Analysis
│   ├── 02_preprocessing_mental_health.ipynb       # Data preprocessing
│   ├── 03_model_training_mental_health.ipynb      # Model training
│   ├── 04_hyperparameter_tuning_mental_health.ipynb # Hyperparameter optimization
│   └── 05_explainbility_mental_health.ipynb       # Model explainability
├── src/
│   ├── data_preprocessing.py  # Data preprocessing utilities
│   ├── predict.py            # Prediction functions
│   ├── train_model.py        # Model training script
│   └── test.py               # Testing utilities
├── app_streamlit.py          # Streamlit web application
├── docker-compose.yml        # Docker Compose configuration
├── Dockerfile               # Docker container definition
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip
- Docker (optional, for containerized deployment)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PsyPredict
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Docker Installation

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

## 🚀 Usage

### Streamlit Web App
```bash
streamlit run app_streamlit.py
```
Access at: http://localhost:8501

### FastAPI REST API
```bash
uvicorn api.app:app --reload
```
Access at: http://localhost:8000
API documentation at: http://localhost:8000/docs

### Jupyter Notebooks
```bash
jupyter notebook
```
Access at: http://localhost:8888

### Model Training
```bash
python src/train_model.py
```

## 📊 Data

The system uses mental health survey data with features including:
- Demographics (Age, Gender, Country)
- Work-related factors (Company size, Remote work, Tech company)
- Mental health indicators (Family history, Work interference)
- Support systems (Benefits, Care options, Wellness programs)

Target variable: `treatment` (whether the person sought mental health treatment)

## 🤖 Models

- **Random Forest**: Primary model with hyperparameter tuning
- **Logistic Regression**: Baseline model for comparison
- **Performance**: ~75% accuracy, 0.79 ROC-AUC

## 🔧 Configuration

### Environment Variables
Create a `.env` file for custom configurations:
```env
MODEL_PATH=models/mental_health_rf_best.pkl
ENCODER_PATH=models/encoders.pkl
API_HOST=0.0.0.0
API_PORT=8000
```

### Model Files
- `models/mental_health_rf_best.pkl`: Best Random Forest model
- `models/encoders.pkl`: Label encoders for categorical variables
- `archive/`: Preprocessed data splits

## 📈 Development

### Adding New Features
1. Create feature branch: `git checkout -b feature/new-feature`
2. Implement changes
3. Test thoroughly
4. Submit pull request

### Code Style
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to functions and classes

## 🧪 Testing

```bash
# Run tests
python -m pytest

# Run specific test file
python src/test.py
```

## 📝 API Documentation

### Prediction Endpoint
```http
POST /predict
Content-Type: application/json

{
  "Age": 30,
  "Gender": "Male",
  "Country": "United States",
  "family_history": "No",
  "work_interfere": "Sometimes",
  ...
}
```

### Response
```json
{
  "prediction": 1,
  "probability": 0.75,
  "explanation": "Feature importance analysis..."
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Mental health survey data contributors
- Open source community for libraries and tools
- Contributors and maintainers

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Contact:  <a href="https://www.linkedin.com/in/bernardofernandezz/">LinkedIn</a>

---

**Note**: This system is for educational and research purposes. It should not be used as a substitute for professional mental health advice or diagnosis.