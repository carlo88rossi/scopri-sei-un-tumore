import streamlit as st
import time

# Configurazione della pagina
st.set_page_config(page_title="Scopri che amico sei 🙂", page_icon="💀", layout="centered")

# Definizione delle domande e delle relative scelte
quiz_data = [
    {
        "question": "Quando esci con i tuoi amici, quale attività preferisci?",
        "choices": ["🎥 Guardare un film insieme", "🍽️ Cenare fuori", "🏞️ Fare una passeggiata", "🎮 Giocare a videogiochi"]
    },
    {
        "question": "Come rispondi quando un amico ha bisogno di aiuto?",
        "choices": ["📞 Lo contatti immediatamente", "🤝 Gli offri il tuo supporto", "🙊 Preferisci non intrometterti", "🕵️ Cerchi di capire la situazione prima di agire"]
    },
    {
        "question": "Quale caratteristica ritieni più importante in un amico?",
        "choices": ["❤️ La lealtà", "😂 Il senso dell'umorismo", "💡 La capacità di dare consigli", "🤗 La sincerità"]
    },
    {
        "question": "Come gestisci le divergenze di opinioni con i tuoi amici?",
        "choices": ["🗣️ Parli apertamente e cerchi un compromesso", "🤐 Eviti il confronto", "😡 Ti arrabbi", "💬 Cerchi di comprendere il loro punto di vista"]
    },
    {
        "question": "Cosa fai per mantenere vive le tue amicizie?",
        "choices": ["📅 Organizzo incontri regolari", "📱 Rimango in contatto tramite messaggi", "🎉 Invito spesso a eventi", "🤝 Offro sempre il mio sostegno"]
    }
]

# Inizializza lo stato della sessione
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "completed" not in st.session_state:
    st.session_state.completed = False

# Titolo dell'app
st.title("🔎 Scopri che amico sei 🙂")

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
