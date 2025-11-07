def predict_clickbait(title, model_components, nb_weight=0.5, rf_weight=0.5):
    import pandas as pd

    questions = ['What', 'How', 'Why', 'Is', 'Are', 'Do', 'Does', 'Did', 'Can', 'Could', 'Will', 'Would']
    pronouns = ['I', 'me', 'my', 'you', 'your', 'he', 'him', 'his', 'she', 'her', 'it', 'its', 'we', 'us', 'our', 'they', 'them', 'their']
    
    modelNB = model_components['nb_model']
    modelRF = model_components['rf_model']
    vectorizer = model_components['vectorizer']
    feature_names = model_components['feature_names']
    
    features = {
        'title_length': len(title),
        'title_world_count': len(title.split()),
        'title_uppercase_count': sum(1 for c in title if c.isupper()),
        'digit_count': sum(1 for c in title if c.isdigit()),
        'has_number': any(c.isdigit() for c in title),
        'starts_with_question': title.startswith(tuple(questions)),
        'contains_question_mark': '?' in title,
        'contains_quotation': '"' in title,
        'contains_pronoun': any(pronoun in title for pronoun in pronouns),
        'average_word_length': sum(len(word) for word in title.split()) / len(title.split()) if len(title.split()) > 0 else 0
    }

    feature_array = pd.DataFrame([[features[col] for col in feature_names]], columns=feature_names)
    
    title_vec = vectorizer.transform([title])
    nb_proba = modelNB.predict_proba(title_vec)[0, 1]
    rf_proba = modelRF.predict_proba(feature_array)[0, 1]
    
    combined_proba = nb_weight * nb_proba + rf_weight * rf_proba
    final_pred = 1 if combined_proba > 0.5 else 0
    
    return {
        'prediction': final_pred,
        'nb_probability': nb_proba,
        'rf_probability': rf_proba,
        'combined_probability': combined_proba
    }
