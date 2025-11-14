# oficiální Python image
FROM python:3.12-slim

# Nastavím pracovní adresář uvnitř kontejneru
# Od teď se všechny příkazy (RUN, CMD, ENTRYPOINT...) spouštějí z /app v kontejneru
WORKDIR /app

# Zkopíruju soubor requirements.txt do image - v souboru je seznam dependencies
COPY app/requirements.txt /app/requirements.txt

# Nainstaluju dependencies
# --no-cache-dir šetří místo – neukládá cache z pipu do image
RUN pip install --no-cache-dir -r requirements.txt

# Zkopíruju vlastni aplikaci (main.py, __init__.py, složku tests, atd.)
COPY app/ /app/

# Otevřu port, na kterém Flask běží (v kontejneru)
EXPOSE 5000

# Definuju příkaz, který se spustí, když kontejner nastartuje - spusti Flask aplikaci
ENTRYPOINT ["python3", "main.py"]

