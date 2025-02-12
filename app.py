import streamlit as st

# Definizione delle domande e delle relative scelte
quiz_data = [
    {
        "question": "Come affronti i problemi quotidiani?",
        "choices": ["Con calma", "Con impazienza", "Ignorandoli", "Con disperazione"]
    },
    {
        "question": "Cosa fai quando ti svegli la mattina?",
        "choices": ["Mediti", "Scorri il telefono", "Fai colazione", "Vai direttamente al lavoro"]
    },
    {
        "question": "Qual è il tuo atteggiamento verso le critiche?",
        "choices": ["Accetti e impari", "Ti arrabbi", "Le ignori", "Usi il sarcasmo"]
    },
    {
        "question": "Come trascorri il tempo libero?",
        "choices": ["Leggi un libro", "Guardi serie TV", "Esci con amici", "Stai in casa"]
    },
    {
        "question": "Qual è la tua reazione quando le cose non vanno come previsto?",
        "choices": ["Cerchi soluzioni", "Ti lamenti", "Ti rassegni", "Trovi scuse"]
    }
]

# Inizializza il contatore della domanda nel session state (se non già presente)
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0

# Titolo dell'app
st.title("Scopri se sei un tumore")

# Controlla se ci sono ancora domande da mostrare
if st.session_state.current_question < len(quiz_data):
    # Recupera la domanda corrente
    question_data = quiz_data[st.session_state.current_question]
    st.header(question_data["question"])
    
    # Crea un bottone per ogni scelta
    for choice in question_data["choices"]:
        if st.button(choice):
            # Incrementa il contatore della domanda e ricarica la pagina
            st.session_state

