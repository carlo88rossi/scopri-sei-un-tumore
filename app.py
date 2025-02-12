import streamlit as st
import time

# Configurazione della pagina
st.set_page_config(page_title="Scopri se sei un tumore", page_icon="💀", layout="centered")

# Definizione delle domande e delle relative scelte
quiz_data = [
    {
        "question": "Come affronti i problemi quotidiani?",
        "choices": ["💆 Con calma", "😡 Con impazienza", "🙈 Ignorandoli", "😱 Con disperazione"]
    },
    {
        "question": "Cosa fai quando ti svegli la mattina?",
        "choices": ["🧘 Mediti", "📱 Scorri il telefono", "🥐 Fai colazione", "🏃 Vai direttamente al lavoro"]
    },
    {
        "question": "Qual è il tuo atteggiamento verso le critiche?",
        "choices": ["🧐 Accetti e impari", "🤬 Ti arrabbi", "😴 Le ignori", "😂 Usi il sarcasmo"]
    },
    {
        "question": "Come trascorri il tempo libero?",
        "choices": ["📖 Leggi un libro", "📺 Guardi serie TV", "🍻 Esci con amici", "🏡 Stai in casa"]
    },
    {
        "question": "Qual è la tua reazione quando le cose non vanno come previsto?",
        "choices": ["🔍 Cerchi soluzioni", "😭 Ti lamenti", "🤷‍♂️ Ti rassegni", "🙃 Trovi scuse"]
    }
]

# Inizializza lo stato della sessione
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "completed" not in st.session_state:
    st.session_state.completed = False

# Titolo dell'app
st.title("🔎 Scopri se sei un tumore")

# Calcola e mostra la barra di avanzamento, garantendo che il valore non superi 1.0
progress = min((st.session_state.current_question + 1) / len(quiz_data), 1.0)
st.progress(progress)

# Controlla se il quiz è finito
if not st.session_state.completed:
    # Mostra la domanda attuale
    question_data = quiz_data[st.session_state.current_question]
    st.subheader(f"📝 Domanda {st.session_state.current_question + 1} di {len(quiz_data)}")
    st.write(question_data["question"])

    # Crea un pulsante per ogni scelta
    for choice in question_data["choices"]:
        if st.button(choice, use_container_width=True):
            # Passa alla domanda successiva
            st.session_state.current_question += 1

            # Se è l'ultima domanda, segnala il completamento
            if st.session_state.current_question >= len(quiz_data):
                st.session_state.completed = True

            st.rerun()  # Ricarica la pagina per aggiornare lo stato
else:
    # **Nasconde tutto il contenuto della pagina prima dell'analisi**
    st.empty()

    # Primo passaggio di suspense con animazione di caricamento (3 secondi invece di 2)
    with st.spinner("🧐 Analizzando le risposte..."):
        time.sleep(5)

    # Passaggio extra di suspense (6 secondi invece di 2)
    st.empty()  # Cancella tutto di nuovo prima di mostrare il nuovo messaggio
    st.info("Nel tuo caso l'analisi sembra richiedere più del previsto...")
    time.sleep(8)

    st.success("✅ I risultati sono pronti!")
    st.header("💀 Sei un tumore!")
    st.markdown("### 😈 Complimenti! Il test ha confermato i tuoi peggiori sospetti.")
    st.image("https://media.giphy.com/media/cjWfHwdAD170ADNlqp/giphy.gif", use_container_width=True)

    # Pulsante per rifare il test
    if st.button("🔄 Rifai il test", use_container_width=True):
        st.session_state.current_question = 0
        st.session_state.completed = False
        st.rerun()
