import numpy as np
import streamlit as st
from keras.models import load_model
from PIL import Image

# Load the model
model = load_model('medicinalleaves2.h5')



#Loading the Model
model = load_model('medicinalleaves2.h5')

#Name of Classes
CLASS_NAMES = ['Aloevera',
 'Amla',
 'Amruthaballi',
 'Arali',
 'Astma_weed',
 'Badipala',
 'Balloon_Vine',
 'Bamboo',
 'Beans',
 'Betel',
 'Bhrami',
 'Bringaraja',
 'Caricature',
 'Castor',
 'Catharanthus',
 'Chakte',
 'Chilly',
 'Citron lime (herelikai)',
 'Coffee',
 'Common rue(naagdalli)',
 'Coriender',
 'Curry',
 'Doddpathre',
 'Drumstick',
 'Ekka',
 'Eucalyptus',
 'Ganigale',
 'Ganike',
 'Gasagase',
 'Ginger',
 'Globe Amarnath',
 'Guava',
 'Henna',
 'Hibiscus',
 'Honge','Insulin','Jackfruit','Jasmine','Kambajala','Kasambruga','Kohlrabi','Lantana','Lemon','Lemongrass','Malabar_Nut','Malabar_Spinach','Mango','Marigold','Mint','Neem','Nelavembu','Nerale','Nooni','Onion','Padri','Palak(Spinach)','Papaya','Parijatha','Pea','Pepper','Pomoegranate','Pumpkin','Raddish','Rose','Sampige','Sapota','Seethaashoka','Seethapala','Spinach1','Tamarind','Taro','Tecoma','Thumbe','Tomato','Tulsi','Turmeric','ashoka','camphor','kamakasturi','kepala']

properties=[
    # Aloe Vera
    ['Aloe Vera',
     'Skin healing and rejuvenation',
     'Anti-inflammatory properties',
     'Digestive aid',
     'Wound healing'],
    
    # Amla
    ['Amla',
     'Rich source of Vitamin C',
     'Antioxidant properties',
     'Boosts immunity',
     'Promotes hair health'],
    
    # Amruthaballi
    ['Amruthaballi',
     'Boosts immunity',
     'Anti-inflammatory effects',
     'Antioxidant properties',
     'Detoxifies the body'],
    
    # Arali
    ['Arali',
     'Cardiac tonic (in controlled doses)',
     'Antipyretic (fever-reducing)',
     'Used in traditional medicine for heart ailments (with caution)',
     'Antifungal properties'],
    
    # Asthma Weed
    ['Asthma Weed',
     'Used for asthma and respiratory issues',
     'Anti-inflammatory effects on the respiratory system',
     'Expectorant properties',
     'Relieves cough'],
    
    # Badipala
    ['Badipala',
     'Anti-inflammatory properties',
     'Used for cough and respiratory issues',
     'Aids digestion',
     'Relieves sore throat'],
    
    # Balloon Vine
    ['Balloon Vine',
     'Anti-inflammatory effects',
     'Analgesic properties (pain relief)',
     'Used for skin diseases',
     'May have diuretic effects'],
    
    # Bamboo
    ['Bamboo',
     'Antioxidant properties',
     'Strengthens hair and nails',
     'Used in traditional medicine for fevers',
     'Supports bone health'],
    
    # Beans
    ['Beans',
     'Rich in protein and fiber',
     'Lowers cholesterol levels',
     'Regulates blood sugar',
     'Good for heart health'],
    
    # Betel
    ['Betel',
     'Aids in digestion',
     'Antimicrobial properties',
     'Stimulates saliva production',
     'Used traditionally for oral health'],
    
    # Bhrami
    ['Bhrami',
     'Improves cognitive function',
     'Reduces anxiety and stress',
     'Enhances memory',
     'Anti-inflammatory effects'],
    
    # Bringaraja
    ['Bringaraja',
     'Stimulates hair growth',
     'Liver tonic',
     'Anti-inflammatory properties',
     'Used in traditional medicine for skin conditions and liver disorders'],
    
    # Caricature
    ['Caricature',
     'Used for skin ailments',
     'Antioxidant properties',
     'May aid in wound healing',
     'May have anti-inflammatory effects'],
    
    # Castor
    ['Castor',
     'Laxative properties',
     'Moisturizes skin',
     'May induce labor (caution)',
     'Used in traditional medicine for joint pain'],
    
    # Catharanthus
    ['Catharanthus',
     'Used in cancer treatment (Vinca alkaloids)',
     'Antidiabetic properties',
     'May lower blood pressure',
     'May have antimicrobial effects'],
    
    # Chakte
    ['Chakte',
     'Used traditionally for digestive issues',
     'May have anti-inflammatory effects',
     'May help with pain relief',
     'Antioxidant properties'],
    
    # Chilly
    ['Chilly',
     'Rich in Vitamin C',
     'May boost metabolism',
     'May help in pain relief (topical use)',
     'Antioxidant properties'],
    
    # Citron lime (herelikai)
    ['Citron lime (herelikai)',
     'Rich in Vitamin C',
     'May aid in digestion',
     'May have antibacterial properties',
     'Used for skin conditions'],
    
    # Coffee
    ['Coffee',
     'Contains caffeine',
     'May improve mental alertness',
     'Antioxidant properties',
     'May have diuretic effects'],
    
    # Common rue (naagdalli)
    ['Common rue (naagdalli)',
     'Used in traditional medicine for joint pain',
     'May have antifungal properties',
     'May aid in digestion',
     'Caution: Toxic in high doses'],
    
    # Coriander
    ['Coriander',
     'Rich in antioxidants',
     'May have antimicrobial properties',
     'May aid in digestion',
     'Used in traditional medicine for skin conditions'],
    
    # Curry
    ['Curry',
     'Anti-inflammatory effects',
     'May aid in digestion',
     'Antioxidant properties',
     'Used in traditional medicine for joint pain'],
    
    # Doddpathre
    ['Doddpathre',
     'May have anti-inflammatory effects',
     'Used for cough and respiratory issues',
     'May aid in digestion',
     'May help with skin conditions'],
    
    # Drumstick
    ['Drumstick',
     'Rich in vitamins and minerals',
     'May aid in digestion',
     'May help boost immunity',
     'Used for joint pain'],
    
    # Ekka
    ['Ekka',
     'Used in traditional medicine for fever',
     'May have antimicrobial properties',
     'May aid in wound healing',
     'Caution: Toxic in high doses'],
    
    # Eucalyptus
    ['Eucalyptus',
     'Used for respiratory issues',
     'May have antimicrobial properties',
     'May aid in wound healing',
     'Used in topical ointments'],
    
    # Ganigale
    ['Ganigale',
     'Used in traditional medicine for digestive issues',
     'May have anti-inflammatory effects',
     'May aid in wound healing',
     'May help with joint pain'],
    
      ['Ganike',
     'Used in traditional medicine for digestive issues',
     'May have anti-inflammatory effects',
     'May aid in wound healing',
     'May help with joint pain'],
    
    ['Gasagase',
     'Rich in healthy fats',
     'May aid in pain relief',
     'Used for digestive issues',
     'May help in skincare'],
     
    # Ginger
    ['Ginger',
     'Anti-inflammatory effects',
     'Aids digestion',
     'May help with nausea',
     'May lower blood sugar levels'],
    
    # Globe Amarnath
    ['Globe Amarnath',
     'Used in traditional medicine for respiratory issues',
     'May have antioxidant properties',
     'May help in wound healing',
     'May have anti-inflammatory effects'],
    
    # Guava
    ['Guava',
     'Rich in Vitamin C',
     'May aid in digestion',
     'Antioxidant properties',
     'May help in boosting immunity'],
    
    # Henna
    ['Henna',
     'Used for hair dyeing',
     'May have antibacterial properties',
     'Used in traditional medicine for skin conditions',
     'May help in wound healing'],
    
    # Hibiscus
    ['Hibiscus',
     'May help in lowering blood pressure',
     'Rich in antioxidants',
     'May aid in digestion',
     'May have anti-inflammatory effects'],
    
    # Honge
    ['Honge',
     'Used in traditional medicine for joint pain',
     'May have anti-inflammatory effects',
     'May aid in wound healing',
     'Caution: Toxic in high doses'],
    
    # Insulin
    ['Insulin',
     'Used in diabetes treatment',
     'Regulates blood sugar levels',
     'May have anti-inflammatory effects',
     'Helps in metabolism'],
    
    # Jackfruit
    ['Jackfruit',
     'Rich in vitamins and minerals',
     'May aid in digestion',
     'May help in boosting immunity',
     'May have antioxidant properties'],
    
    # Jasmine
    ['Jasmine',
     'Used in aromatherapy',
     'May have calming effects',
     'May aid in reducing stress',
     'Used in traditional medicine for skin conditions'],
    
    # Kambajala
    ['Kambajala',
     'Used for joint pain',
     'May have anti-inflammatory effects',
     'May aid in digestion',
     'May help in boosting immunity'],
    
    # Kasambruga
    ['Kasambruga',
     'Used in traditional medicine for respiratory issues',
     'May aid in wound healing',
     'May have anti-inflammatory effects',
     'May have antimicrobial properties'],
    
    # Kohlrabi
    ['Kohlrabi',
     'Rich in vitamins and minerals',
     'May aid in digestion',
     'May help in maintaining healthy bones',
     'May have antioxidant properties'],
    
    # Lantana
    ['Lantana',
     'Used in traditional medicine for skin conditions',
     'May have antimicrobial properties',
     'May aid in wound healing',
     'Caution: Toxic in high doses'],
    
    # Lemon
    ['Lemon',
     'Rich in Vitamin C',
     'May aid in digestion',
     'Antioxidant properties',
     'Used in traditional medicine for cold and sore throat'],
    
    # Lemongrass
    ['Lemongrass',
     'May help in reducing stress and anxiety',
     'May aid in digestion',
     'Antioxidant properties',
     'Used in aromatherapy'],
    
    # Malabar Nut
    ['Malabar Nut',
     'Used in respiratory conditions',
     'May aid in cough relief',
     'May have bronchodilator effects',
     'May help in asthma management'],
    
    # Malabar Spinach
    ['Malabar Spinach',
     'Rich in vitamins and minerals',
     'May help in boosting immunity',
     'May aid in digestion',
     'May have antioxidant properties'],
    
    # Mango
    ['Mango',
     'Rich in vitamins and minerals',
     'Antioxidant properties',
     'May aid in digestion',
     'May help in boosting immunity'],
    
    # Marigold
    ['Marigold',
     'Used in traditional medicine for skin conditions',
     'May have antimicrobial properties',
     'May aid in wound healing',
     'May help in eye health'],
    
    # Mint
    ['Mint',
     'May aid in digestion',
     'May help in relieving headaches',
     'Antioxidant properties',
     'Used in aromatherapy'],
    
    # Neem
    ['Neem',
     'Antibacterial and antifungal properties',
     'Used in skincare',
     'May aid in dental health',
     'May help in boosting immunity'],
    
    # Nelavembu
    ['Nelavembu',
     'Used in traditional medicine for fever',
     'May have anti-inflammatory effects',
     'May aid in liver health',
     'May help in boosting immunity'],
    
    # Nerale
    ['Nerale',
     'May help in digestion',
     'May have anti-inflammatory effects',
     'May aid in wound healing',
     'May help in boosting immunity'],
    
    # Nooni
    ['Nooni',
     'Used in traditional medicine for fever',
     'May have antioxidant properties',
     'May aid in digestion',
     'May help in boosting immunity'],
    
    # Onion
    ['Onion',
     'Antioxidant properties',
     'May help in reducing cholesterol',
     'May aid in regulating blood sugar',
     'May have anti-inflammatory effects'],
    
    # Padri
    ['Padri',
     'Used in traditional medicine for joint pain',
     'May have anti-inflammatory effects',
     'May aid in digestion',
     'May help in boosting immunity'],
    
    # Palak (Spinach)
    ['Palak (Spinach)',
     'Rich in vitamins and minerals',
     'May aid in digestion',
     'May help in boosting immunity',
     'May have antioxidant properties'],
    
    # Papaya
    ['Papaya',
     'Rich in vitamins and minerals',
     'May aid in digestion',
     'May have antioxidant properties',
     'May help in skin conditions'],
    
    # Parijatha
    ['Parijatha',
     'Used in traditional medicine for skin conditions',
     'May have antimicrobial properties',
     'May aid in wound healing',
     'May help in reducing fever'],
    
    # Pea
    ['Pea',
     'Rich in protein and fiber',
     'May aid in digestion',
     'May help in maintaining blood sugar levels',
     'May have antioxidant properties'],
    
    # Pepper
    ['Pepper',
     'May aid in digestion',
     'May have antioxidant properties',
     'May help in improving metabolism',
     'May have anti-inflammatory effects'],
    
    # Pomegranate
    ['Pomegranate',
     'Rich in antioxidants',
     'May aid in heart health',
     'May have anti-inflammatory effects',
     'May help in maintaining blood pressure'],
    
    # Pumpkin
    ['Pumpkin',
     'Rich in vitamins and minerals',
     'May aid in digestion',
     'May help in eye health',
     'May have antioxidant properties'],
    
    # Radish
    ['Radish',
     'May aid in digestion',
     'May have diuretic properties',
     'May help in regulating blood pressure',
     'May have antioxidant properties'],
    
    # Rose
    ['Rose',
     'Used in aromatherapy',
     'May aid in reducing stress and anxiety',
     'May have anti-inflammatory effects',
     'Used in skincare'],
    
    # Sampige
    ['Sampige',
     'Used in traditional medicine for joint pain',
     'May have anti-inflammatory effects',
     'May aid in digestion',
     'May help in boosting immunity'],
    
    # Sapota
    ['Sapota',
     'Rich in vitamins and minerals',
     'May aid in digestion',
     'May help in boosting immunity',
     'May have antioxidant properties'],
    
    # Seethaashoka
    ['Seethaashoka',
     'Used in traditional medicine for gynecological issues',
     'May aid in menstrual health',
     'May have antimicrobial properties',
     'May help in reducing inflammation'],
    
    # Seethapala
    ['Seethapala',
     'May aid in digestion',
     'May help in boosting immunity',
     'May have antioxidant properties',
     'May help in maintaining skin health'],
    
    # Spinach1
    ['Spinach1',
     'Rich in vitamins and minerals',
     'May aid in digestion',
     'May help in boosting immunity',
     'May have antioxidant properties'],
    
    # Tamarind
    ['Tamarind',
     'May aid in digestion',
     'May have antioxidant properties',
     'May have anti-inflammatory effects',
     'May help in skin conditions'],
    
    # Taro
    ['Taro',
     'Rich in vitamins and minerals',
     'May aid in digestion',
     'May have antioxidant properties',
     'May help in regulating blood sugar'],
    
    # Tecoma
    ['Tecoma',
     'Used in traditional medicine for fever',
     'May have antimicrobial properties',
     'May aid in wound healing',
     'May help in reducing inflammation'],
    
    # Thumbe
    ['Thumbe',
     'Used in traditional medicine for joint pain',
     'May have anti-inflammatory effects',
     'May aid in digestion',
     'May help in boosting immunity'],
    
    # Tomato
    ['Tomato',
     'Rich in antioxidants',
     'May aid in heart health',
     'May have anti-inflammatory effects',
     'May help in maintaining blood pressure'],
    
     # Tulsi
    ['Tulsi',
     'Used in traditional medicine for respiratory issues',
     'May aid in cough relief',
     'May help in reducing stress and anxiety',
     'May have antimicrobial properties'],

    # Turmeric
    ['Turmeric',
     'Anti-inflammatory effects',
     'Antioxidant properties',
     'May aid in wound healing',
     'May help in digestive health'],

    # Ashoka
    ['Ashoka',
     'Used in traditional medicine for gynecological issues',
     'May aid in menstrual health',
     'May help in reducing inflammation',
     'May have antimicrobial properties'],

    # Camphor
    ['Camphor',
     'Used in pain relief ointments',
     'May aid in respiratory issues',
     'May help in skin conditions',
     'Caution: Toxic in high doses'],

    # Kamakasturi
    ['Kamakasturi',
     'Used in traditional medicine for skin conditions',
     'May aid in wound healing',
     'May have anti-inflammatory effects',
     'Used in aromatherapy'],

    # Kepala
    ['Kepala',
     'May aid in digestion',
     'May help in reducing inflammation',
     'May have antimicrobial properties',
     'May have antioxidant properties']
]

# Setting Title of App
st.title("Medicinal Plant Identification")
st.markdown("Upload an image of the Plant")

# Uploading the plant image
plant_image = st.file_uploader("Choose an image...", type="jpg")
submit = st.button('Predict')

# On predict button click
if submit:
    if plant_image is not None:
        # Open image using Pillow
        image = Image.open(plant_image)

        # Displaying the image
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Resizing the image
        image = image.resize((299, 299))

        # Convert image to numpy array
        image_np = np.array(image)

        # Expand dimensions to match model input shape
        image_np = np.expand_dims(image_np, axis=0)

        # Make prediction
        Y_pred = model.predict(image_np)

        # Display the prediction
        predicted_class = CLASS_NAMES[np.argmax(Y_pred)]
        st.title(f"The Plant Species is {predicted_class}")
        st.title("\nProperties-")

        # Display the properties of the predicted plant
        for property in properties[np.argmax(Y_pred)]:
            st.text(property)

# Footer
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: right;
            padding: 10px 0;
        }
    </style>
    <div class="footer">
        Made by Shivam Kumar Jha
    </div>
""", unsafe_allow_html=True)
