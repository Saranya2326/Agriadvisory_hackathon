"""Multilingual rule-based crop advisory system.
This is a transparent demo, not a trained AI model.
"""

CROP_GUIDANCE = {
    "rice": {
        "en": "For rice, monitor field water levels, crop growth and nutrient needs. Follow locally recommended cultivation practices.",
        "ta": "நெற்பயிரில் நீர் நிலை, பயிர் வளர்ச்சி மற்றும் ஊட்டச்சத்து தேவைகளை தொடர்ந்து கவனிக்கவும். உள்ளூர் பரிந்துரைகளைப் பின்பற்றவும்.",
        "hi": "धान में पानी का स्तर, फसल की वृद्धि और पोषक तत्वों की आवश्यकता पर ध्यान दें। स्थानीय सिफारिशों का पालन करें।"
    },
    "tomato": {
        "en": "For tomato, monitor leaf symptoms, soil moisture and plant growth. Avoid excessive watering.",
        "ta": "தக்காளியில் இலை அறிகுறிகள், மண் ஈரப்பதம் மற்றும் செடி வளர்ச்சியை கவனிக்கவும். அதிகப்படியான நீர்ப்பாசனத்தைத் தவிர்க்கவும்.",
        "hi": "टमाटर में पत्तियों के लक्षण, मिट्टी की नमी और पौधों की वृद्धि पर ध्यान दें। अधिक सिंचाई से बचें।"
    },
    "groundnut": {
        "en": "For groundnut, maintain suitable soil moisture and monitor for leaf spots and pest symptoms.",
        "ta": "நிலக்கடலையில் ஏற்ற மண் ஈரப்பதத்தை பராமரிக்கவும். இலைப்புள்ளி மற்றும் பூச்சி அறிகுறிகளை கவனிக்கவும்.",
        "hi": "मूँगफली में उचित मिट्टी की नमी बनाए रखें और पत्ती धब्बों तथा कीटों के लक्षणों पर ध्यान दें।"
    }
}

TOPIC_GUIDANCE = {
    "water": {
        "en": "Water management: Check soil moisture and field conditions regularly. Avoid both waterlogging and unnecessary water use. Irrigation needs depend on crop stage and soil type.",
        "ta": "நீர் மேலாண்மை: மண் ஈரப்பதம் மற்றும் வயல் நிலையை தொடர்ந்து கவனிக்கவும். அதிக நீர் தேங்குவதையும் தேவையற்ற நீர்ப்பாசனத்தையும் தவிர்க்கவும். பயிரின் வளர்ச்சி நிலை மற்றும் மண் வகைக்கு ஏற்ப நீர் தேவை மாறும்.",
        "hi": "सिंचाई: मिट्टी की नमी और खेत की स्थिति नियमित रूप से जाँचें। जलभराव और अनावश्यक सिंचाई से बचें। पानी की आवश्यकता फसल की अवस्था और मिट्टी पर निर्भर करती है।"
    },
    "yellow": {
        "en": "Yellow leaves can be caused by nutrient deficiency, excess water, pests or disease. Check which leaves are affected and inspect the roots and soil. Seek local agricultural advice before applying treatment.",
        "ta": "இலைகள் மஞ்சளாவதற்கு ஊட்டச்சத்து குறைபாடு, அதிக நீர், பூச்சி அல்லது நோய் காரணமாக இருக்கலாம். எந்த இலைகள் பாதிக்கப்பட்டுள்ளன என்பதை கவனித்து, வேர் மற்றும் மண்ணை பரிசோதிக்கவும். சிகிச்சை அளிப்பதற்கு முன் வேளாண்மை அலுவலரிடம் ஆலோசனை பெறவும்.",
        "hi": "पत्तियों का पीला होना पोषक तत्वों की कमी, अधिक पानी, कीट या बीमारी के कारण हो सकता है। प्रभावित पत्तियों, जड़ों और मिट्टी की जाँच करें। उपचार से पहले कृषि अधिकारी से सलाह लें।"
    },
    "pest": {
        "en": "Pest management: Inspect both sides of leaves and check for insects, eggs and damage. Identify the pest before choosing a control method. Follow locally approved recommendations.",
        "ta": "பூச்சி மேலாண்மை: இலைகளின் இருபுறங்களையும் பரிசோதித்து பூச்சிகள், முட்டைகள் மற்றும் சேதங்களை கவனிக்கவும். கட்டுப்பாட்டு முறையைத் தேர்வு செய்வதற்கு முன் பூச்சியை அடையாளம் காணவும். உள்ளூர் அங்கீகரிக்கப்பட்ட பரிந்துரைகளைப் பின்பற்றவும்.",
        "hi": "कीट प्रबंधन: पत्तियों के दोनों तरफ की जाँच करें और कीट, अंडे तथा नुकसान देखें। नियंत्रण का तरीका चुनने से पहले कीट की पहचान करें। स्थानीय स्वीकृत सलाह अपनाएँ।"
    },
    "disease": {
        "en": "Disease management: Observe spots, unusual colour changes, wilting and spreading symptoms. Take clear photos and consult an agriculture officer or KVK before using any treatment.",
        "ta": "நோய் மேலாண்மை: இலைப்புள்ளிகள், நிறமாற்றம், வாடுதல் மற்றும் பரவும் அறிகுறிகளை கவனிக்கவும். சிகிச்சை பயன்படுத்துவதற்கு முன் தெளிவான புகைப்படங்களை எடுத்து வேளாண்மை அலுவலர் அல்லது KVK-யிடம் ஆலோசனை பெறவும்.",
        "hi": "रोग प्रबंधन: पत्तियों के धब्बे, रंग में बदलाव, मुरझाना और फैलते लक्षण देखें। उपचार से पहले स्पष्ट तस्वीरें लेकर कृषि अधिकारी या KVK से सलाह लें।"
    },
    "fertilizer": {
        "en": "Fertilizer guidance: The correct fertilizer and quantity depend on soil test results, crop stage and local recommendations. Avoid applying fertilizer without checking crop requirements.",
        "ta": "உர வழிகாட்டுதல்: சரியான உரம் மற்றும் அளவு மண் பரிசோதனை முடிவு, பயிரின் வளர்ச்சி நிலை மற்றும் உள்ளூர் பரிந்துரைகளைப் பொறுத்தது. பயிரின் தேவையை அறியாமல் உரமிட வேண்டாம்.",
        "hi": "उर्वरक सलाह: सही उर्वरक और मात्रा मिट्टी की जाँच, फसल की अवस्था और स्थानीय सिफारिशों पर निर्भर करती है। फसल की आवश्यकता जाने बिना उर्वरक न डालें।"
    },
    "growth": {
        "en": "Crop growth: Use good-quality seeds, maintain suitable soil moisture, remove weeds and monitor the crop regularly. Follow cultivation guidance suitable for your region.",
        "ta": "பயிர் வளர்ச்சி: தரமான விதைகளைப் பயன்படுத்தவும், மண் ஈரப்பதத்தை பராமரிக்கவும், களைகளை அகற்றவும், பயிரை தொடர்ந்து கண்காணிக்கவும். உங்கள் பகுதிக்கு ஏற்ற சாகுபடி முறைகளைப் பின்பற்றவும்.",
        "hi": "फसल की वृद्धि: अच्छी गुणवत्ता वाले बीजों का उपयोग करें, मिट्टी की उचित नमी बनाए रखें, खरपतवार हटाएँ और फसल की नियमित निगरानी करें। अपने क्षेत्र के अनुसार खेती की सलाह अपनाएँ।"
    }
}

KEYWORDS = {
    "water": [
        "water", "irrigation", "watering", "rain", "thanni", "neer",
        "தண்ணீர்", "நீர்", "பாசனம்", "மழை",
        "पानी", "सिंचाई", "बारिश"
    ],
    "yellow": [
        "yellow", "yellowing", "leaves turning yellow", "leaf yellow",
        "manjal", "மஞ்சள்", "மஞ்சளாக", "இலை மஞ்சள்",
        "पीला", "पीली", "पत्ते पीले"
    ],
    "pest": [
        "pest", "insect", "insects", "bug", "worm", "caterpillar",
        "poochi", "பூச்சி", "புழு", "பூச்சிகள்",
        "कीट", "कीड़े", "इल्ली"
    ],
    "disease": [
        "disease", "infection", "fungus", "fungal", "spots", "rot",
        "noi", "நோய்", "புள்ளி", "அழுகல்",
        "रोग", "बीमारी", "धब्बे", "सड़न"
    ],
    "fertilizer": [
        "fertilizer", "fertiliser", "manure", "urea", "nutrient",
        "ur", "uram", "உரம்", "உரங்கள்", "ஊட்டச்சத்து",
        "खाद", "उर्वरक", "पोषक तत्व"
    ],
    "growth": [
        "grow", "growth", "cultivation", "planting", "seed",
        "valara", "valar", "வளர்க்க", "வளர்ச்சி", "விதை", "சாகுபடி",
        "उगाना", "बढ़ना", "विकास", "बीज", "खेती"
    ]
}

MESSAGES = {
    "en": (
        "Crop advisory",
        "This is general information, not a field diagnosis. For a specific recommendation, share crop photos and symptoms with your local agriculture officer or KVK."
    ),
    "ta": (
        "பயிர் ஆலோசனை",
        "இது பொதுவான தகவல் மட்டுமே; வயல் ஆய்வு அல்ல. குறிப்பிட்ட பரிந்துரைக்கு பயிரின் புகைப்படங்கள் மற்றும் அறிகுறிகளை உள்ளூர் வேளாண்மை அலுவலர் அல்லது KVK-யிடம் தெரிவிக்கவும்."
    ),
    "hi": (
        "फसल सलाह",
        "यह सामान्य जानकारी है, खेत का निदान नहीं। विशेष सलाह के लिए फसल की तस्वीरें और लक्षण स्थानीय कृषि अधिकारी या KVK को बताएँ।"
    )
}


def get_advisory(crop, question, language="en"):
    language = language if language in ("en", "ta", "hi") else "en"

    crop_key = (crop or "").strip().lower()
    question_text = (question or "").strip().lower()

    # Identify the question topic
    selected_topic = None

    for topic, keywords in KEYWORDS.items():
        if any(word in question_text for word in keywords):
            selected_topic = topic
            break

    # Select the answer
    if selected_topic:
        answer = TOPIC_GUIDANCE[selected_topic][language]

    elif crop_key in CROP_GUIDANCE:
        answer = CROP_GUIDANCE[crop_key][language]

    else:
        answer = {
            "en": "Please provide a valid crop name and describe the farming problem. You can ask about water, yellow leaves, pests, diseases or fertilizers.",
            "ta": "சரியான பயிரின் பெயரையும் விவசாயப் பிரச்சினையையும் குறிப்பிடவும். தண்ணீர், மஞ்சள் இலைகள், பூச்சிகள், நோய்கள் அல்லது உரங்கள் பற்றி கேட்கலாம்.",
            "hi": "कृपया फसल का सही नाम और समस्या बताएँ। आप पानी, पीली पत्तियों, कीटों, रोगों या उर्वरकों के बारे में पूछ सकते हैं।"
        }[language]

    title, note = MESSAGES[language]

    return {
        "title": title,
        "answer": answer,
        "note": note,
        "method": "multilingual-keyword-rule-based-demo"
    }