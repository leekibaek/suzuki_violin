mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
healess = true\n\
\n\
" > ~/.streamlit/config.tom1
