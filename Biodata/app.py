import streamlit as st

from PIL import Image
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Portfolio Fauzan",
    page_icon="👤",
    layout="centered" # "centered" lebih rapi untuk profil
)

# --- CSS KUSTOM (Untuk styling opsional) ---
# Kita tambahkan CSS untuk membuat foto profil menjadi lingkaran
st.markdown("""
<style>
/* MEMBUAT SEMUA FONT HITAM DENGAN GLOW PUTIH */
    h1, h2, h3, h4, h5, h6, p, span, div, label, li {{
        color: #000000 !important;
        text-shadow: 
            -1px -1px 0 #FFFFFF,  
             1px -1px 0 #FFFFFF,
            -1px  1px 0 #FFFFFF,  
             1px  1px 0 #FFFFFF,
             0px  0px 10px #FFFFFF; /* Efek glow agar terbaca */
        font-weight: 600;
    }}
    /* Membuat gambar profil menjadi lingkaran dan berbayang */
    .profile-pic {
        border-radius: 50%;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border: 4px solid white; /* Memberi border putih tipis */
    }
</style>
""", unsafe_allow_html=True)


# --- 1. SEKSI HEADER (DENGAN FOTO DI KIRI) ---
with st.container():
    # Membuat dua kolom: [kolom_kiri_foto, kolom_kanan_teks]
    # Angka [1, 3] berarti kolom kanan 3x lebih lebar dari kolom kiri.
    col_foto, col_teks = st.columns([1, 3])
    
    # --- Kolom Kiri: Menampilkan Foto ---
    with col_foto:
        # Cek apakah file foto ada
        file_foto = "foto_fauzan.jpg" # GANTI DENGAN NAMA FILE FOTO ANDA
        
        if os.path.exists(file_foto):
            # Buka gambar dengan PIL
            image = Image.open(file_foto)
            # Tampilkan gambar dengan styling CSS kustom (lingkaran)
            st.image("foto_fauzan.jpg", use_container_width=True)
            # Catatan: use_column_width=True akan menyesuaikan ukuran gambar dengan lebar kolom
        else:
            # Jika foto tidak ditemukan, tampilkan placeholder abu-abu
            st.warning(f"File '{file_foto}' tidak ditemukan di folder ini.")
            st.image("https://via.placeholder.com/150", use_column_width=True)

    # --- Kolom Kanan: Menampilkan Teks Sambutan ---
    with col_teks:
        st.subheader("Halo, saya Fauzan! 👋")
        st.title("Seorang Python Developer dari Jakarta")
        st.write(
            "Saya senang membangun solusi digital yang memudahkan pekerjaan orang lain. "
            "Fokus saya adalah pada automasi, pengolahan data, dan pembuatan aplikasi web."
        )
        st.write("[Pelajari lebih lanjut >](https://www.linkedin.com/in/fauzan-afif-ab907737a/)") # Ganti link

# --- 2. SEKSI TENTANG SAYA ---
with st.container():
    st.write("---") # Garis pemisah
    col_tentang, col_funfact = st.columns([3, 2])
    
    with col_tentang:
        st.header("Tentang Saya")
        st.write(
            """
            Saya adalah seorang profesional yang berdedikasi dengan pengalaman dalam:
            - Pengembangan aplikasi web menggunakan Streamlit, Flask, atau Django.
            - Analisis data dan visualisasi interaktif.
            - Otomatisasi tugas-tugas repetitif dengan skrip Python.
            
            Jika Anda memiliki proyek menarik atau ingin berdiskusi, jangan ragu untuk menghubungi saya.
            """
        )
    
    with col_funfact:
        # Menampilkan Fun Fact dalam info box seperti di gambar Anda
        st.write("##") # Memberi sedikit spasi di atas agar sejajar
        st.info(
            "💡 **Fun Fact:** Saya sangat senang bermain game Mobile Legends. "
            "Dan jangan kaget, Rank saya sudah Mytic, lho!"
        )

# --- SEKSI SKILLS (Tambahan opsional agar lebih penuh) ---
with st.container():
    st.write("---")
    st.header("Keahlian Utama")
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.subheader("Bahasa")
        st.write("Python, SQL, HTML/CSS")
    with col_s2:
        st.subheader("Framework/Lib")
        st.write("Streamlit, Pandas, NumPy")
    with col_s3:
        st.subheader("Tools")
        st.write("Git, Docker, VS Code")

# --- FOOTER ---
st.write("##")
st.markdown("<div style='text-align: center; color: gray;'>©Profil Fauzan</div>", unsafe_allow_html=True)

# 1. KONFIGURASI HALAMAN & TEMA (Harus paling atas)
st.set_page_config(
    page_title="Portfolio Desain Latar Belakang",
    page_icon="🎨",
    layout="centered" # Pilihan: "centered" (rapi) atau "wide" (penuh)
)

# 2. CSS KUSTOM UNTUK LATAR BELAKANG DAN STYLING UTAMA
# Kami menggunakan linear-gradient untuk warna dasar dan radial-gradient untuk pola titik.
custom_css = """
<style>
    /* Mengubah background seluruh aplikasi */
    .stApp {
        background-color: #f0f4f8; /* Warna dasar light gray-blue */
        background-image: 
            radial-gradient(#d1d9e6 1px, transparent 1px), /* Pola titik */
            linear-gradient(135deg, #f0f4f8 0%, #e0eafc 100%); /* Gradien lembut */
        background-size: 20px 20px, 100% 100%; /* Ukuran titik dan gradien */
        background-position: 0 0, 0 0;
    }

    /* Mengubah font global agar lebih modern */
    html, body, [class*="css"]  {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Mempercantik Kontainer Konten Utama */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.9); /* Putih transparan agar background terlihat sedikit */
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); /* Bayangan halus */
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    /* Perbaikan Styling Form (Dari langkah sebelumnya) */
    input[type=text], input[type=email], textarea {
        width: 100%;
        padding: 12px;
        border: 1px solid #ddd;
        border-radius: 8px;
        box-sizing: border-box;
        margin-top: 6px;
        margin-bottom: 16px;
        background-color: #fbfbfb;
    }
    
    button[type=submit] {
        background-color: #4A90E2; /* Warna biru modern */
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    
    button[type=submit]:hover {
        background-color: #357ABD;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Konfigurasi Halaman
st.set_page_config(page_title="Profil Saya", page_icon="👤", layout="centered")



# --- KONTAK ---
with st.container():
    st.write("---")
    st.header("📩 Hubungi Saya")
    st.write("Punya pertanyaan? Kirimkan pesan melalui form di bawah ini:")

    # CSS untuk mempercantik Form
    contact_form_style = """
    <style>
        input[type=text], input[type=email], textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-sizing: border-box;
            margin-top: 6px;
            margin-bottom: 16px;
            resize: vertical;
            font-family: sans-serif;
        }
        button[type=submit] {
            background-color: #007BFF;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
            transition: 0.3s;
        }
        button[type=submit]:hover {
            background-color: #0056b3;
        }
    </style>
    """
    st.markdown(contact_form_style, unsafe_allow_html=True)

    # Form HTML
    contact_form = """
    <form action="https://formsubmit.co/oke.ojan09@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Nama Lengkap" required>
        <input type="email" name="email" placeholder="Alamat Email" required>
        <textarea name="message" placeholder="Tulis pesan Anda di sini..." style="height:150px" required></textarea>
        <button type="submit">Kirim Pesan Sekarang</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    
