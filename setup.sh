mkdir -p ~/.streamlit/
echo "[theme]
primaryColor = '#FF4B4B'
backgroundColor = ‘#f7f7f7’
secondaryBackgroundColor = ‘#ec5c0e’
textColor= ‘#101010’
font = ‘sans-serif’
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
