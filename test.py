import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Memuat file .env
load_dotenv()

# Membuat model LLM dengan Google Generative AI
gemini_10_pro = GoogleGenerativeAI(model="gemini-1.0-pro")

# Template untuk prompt terjemahan
translation_prompt = PromptTemplate(
    template=''' 
    Translate the following sentence into informal English:
    {sentence}
    ''',
    input_variables=["sentence"]
)

# Gabungkan prompt dan model menjadi chain
translation_chain = translation_prompt | gemini_10_pro

# Pengaturan aplikasi Streamlit
st.set_page_config(page_title="Chatbot & Document Reader", layout="wide")

# Tab navigasi
tab1, tab2 = st.tabs(["🤖 Chatbot", "📄 Document Reader"])

# Tab 1: Chatbot
with tab1:
    st.title("🤖 Generative AI Chatbot")
    st.markdown("Tanya apapun atau minta terjemahan (Gunakan format `translate: kalimat`). Ketik `/clear` untuk menghapus percakapan.")

    # Inisialisasi sesi untuk riwayat percakapan
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []

    # Fungsi untuk memproses input pengguna
    def process_input(user_input):
        if user_input.lower() == "/clear":
            # Menghapus riwayat percakapan
            st.session_state["conversation"] = []
            return "Riwayat percakapan telah dihapus."

        if user_input.lower() == "exit":
            return "Goodbye! Refresh the page to start over."

        if user_input.startswith("translate:"):
            # Mode terjemahan
            sentence_to_translate = user_input.replace("translate:", "").strip()
            try:
                translation = translation_chain.invoke({"sentence": sentence_to_translate})
                return f"(Translation): {translation}"
            except Exception as e:
                return f"Error during translation - {e}"
        else:
            # Mode tanya jawab
            try:
                response = gemini_10_pro.invoke(user_input)
                return response
            except Exception as e:
                return f"Error - {e}"

    # Input pengguna
    user_input = st.text_input("Type your message:", key="input_box")

    # Jika ada input dari pengguna, proses dan tambahkan ke percakapan
    if user_input:
        bot_response = process_input(user_input)

        if user_input.lower() != "/clear":  # Hindari menambah ke riwayat jika perintah adalah "/clear"
            st.session_state["conversation"].append({"user": user_input, "bot": bot_response})

        # Reset input box setelah pengiriman
        st.experimental_set_query_params(input_box="")

    # Tampilkan riwayat percakapan
    for chat in st.session_state["conversation"]:
        with st.chat_message("user"):
            st.markdown(f"**You:** {chat['user']}")
        with st.chat_message("assistant"):
            st.markdown(f"**Chatbot:** {chat['bot']}")

# Tab 2: Document Reader
with tab2:
    st.title("📄 Document Reader")
    st.markdown("Unggah dokumen Anda untuk dibaca atau dianalisis oleh AI.")

    # Upload file
    uploaded_file = st.file_uploader("Upload your document (PDF or TXT)", type=["pdf", "txt"])

    if uploaded_file:
        try:
            # Menampilkan isi file
            if uploaded_file.type == "application/pdf":
                from PyPDF2 import PdfReader
                reader = PdfReader(uploaded_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                st.text_area("Content of the PDF", value=text, height=300)
            elif uploaded_file.type == "text/plain":
                text = uploaded_file.read().decode("utf-8")
                st.text_area("Content of the Text File", value=text, height=300)

            # Analisis atau pertanyaan ke dokumen
            question = st.text_input("Ask a question about the document:")
            if question:
                try:
                    response = gemini_10_pro.invoke(question + " based on this document: " + text)
                    st.write(f"Response: {response}")
                except Exception as e:
                    st.write(f"Error: {e}")
        except Exception as e:
            st.error(f"Error reading the file: {e}")
