echo "[+] Starting UWSGI"
./uwsgi.sh &
echo "[+] Starting Engine"
cd app/engine
python engine.py &
cd -
echo "[+] Complete"