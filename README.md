# Clickbait Detector

A machine learning-powered clickbait detection system with a Chrome extension and Flask API backend. This project uses ensemble methods to identify clickbait content with high accuracy, specifically designed to work with YouTube video titles.

## Architecture

```
├── backend/                    # Machine learning and API backend
│   ├── api/                   
│   │   ├── main.py            # Flask API server
│   │   └── utils.py           # Prediction utilities
│   ├── data/                  
│   │   └── clickbait_title_classification.csv  # Training dataset 
│   ├── models/                
│   │   ├── combined.joblib    # Ensemble model
│   │   ├── nb.joblib          # Naive Bayes model
│   │   ├── rf.joblib          # Random Forest model
│   │   └── gb.joblib          # Gradient Boosting model
│   └── notebooks/             
│       └── exploration.ipynb  # Data analysis and model training
├── frontend/                  # Chrome extension
│   ├── manifest.json          # Extension configuration
│   ├── popup.html/js/css      # Extension popup interface
│   └── scripts/               
│       └── content.js         # YouTube integration script
└── test/                      # Test suite
    └── test_predict.py        # Model prediction tests
```

## Features

### Machine Learning Models
- **Naive Bayes Classifier**: Text-based feature analysis using TF-IDF vectorization
- **Random Forest(RF) Classifier**: Engineered feature analysis
- **Ensemble Method**: Weighted combination of both models for improved accuracy

### Feature Engineering
RF classifier analyzes multiple aspects of titles:
- **Linguistic Features**: Question words, pronouns, punctuation patterns
- **Statistical Features**: Title length, word count, character distribution
- **Formatting Features**: Uppercase count, digit presence, quotation marks
- **Semantic Features**: Average word length, question mark presence

### Chrome Extension
- **Real-time Detection**: Automatically analyzes YouTube video titles
- **Visual Indicators**: Displays clickbait probability percentage
- **Non-intrusive**: Seamlessly integrates with YouTube's interface

## Installation

### Prerequisites
- Python 3.7+
- Chrome/Chromium browser
- Node.js (optional, for development)

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/NikitaBryndak/clickbait-detector.git
   cd clickbait-detector
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask API server**
   ```bash
   cd backend/api
   python main.py
   ```
   The API will be available at `http://localhost:8000`

### Chrome Extension Setup

1. **Open Chrome Extensions page**
   - Navigate to `chrome://extensions/`
   - Enable "Developer mode"

2. **Load the extension**
   - Click "Load unpacked"
   - Select the `frontend` folder

3. **Verify installation**
   - The extension icon should appear in the toolbar
   - Visit any YouTube video to see clickbait detection in action

## API Usage

### Health Check
```bash
GET http://localhost:8000/health
```

### Predict Clickbait
```bash
POST http://localhost:8000/predict
Content-Type: application/json

{
    "title": "You Won't Believe What Happened Next!"
}
```

**Example Response:**
```json
{
    "prediction": 1,
    "nb_probability": 0.892,
    "rf_probability": 0.756,
    "combined_probability": 0.824
}
```

##  Privacy & Security

- **Local Processing**: All analysis happens locally or on your controlled server
- **No Data Collection**: The extension doesn't store or transmit personal data
- **Minimal Permissions**: Only requires access to YouTube and localhost API

##  Development Status

**Current Version**: 0.1 

**Implemented Features**:
- ✅ Core ML models (NB + RF ensemble)
- ✅ Flask API with health monitoring
- ✅ Chrome extension with YouTube integration
- ✅ Feature engineering pipeline
- ✅ Language translation support

**Upcoming Features**:
- 🔄 Enhanced popup interface
- 🔄 Additional social media platform support
- 🔄 Model retraining pipeline
- 🔄 Performance analytics dashboard
- 🔄 Comprehensive test suite

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
