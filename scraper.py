import json
import time
from datetime import datetime

# Aquí importaremos curl_cffi en el futuro para evadir bloqueos
# from curl_cffi import requests

def fetch_viral_trends():
    print(f"[{datetime.now()}] Iniciando motor de TrendGrid...")
    
    try:
        print("Simulando extracción de datos de TikTok y YouTube...")
        time.sleep(2)
        
        # Estos son los datos frescos que tu web leerá automáticamente
        scraped_data = [
            {
                "type": "niche",
                "title": "Faceless Personal Finance (Stickman)",
                "platform": "yt",
                "platformLabel": "YouTube",
                "rpm": "$22.00",
                "saturation": "Medium",
                "satColor": "yellow",
                "desc": "Explaining credit cards and Roth IRAs using simple animations.",
                "hook": "The banks are lying to you about your savings account...",
                "arbitrage": False
            },
            {
                "type": "video",
                "title": "I Tested the Cheapest Tech Gadgets on Amazon",
                "platform": "tt",
                "platformLabel": "TikTok",
                "vph": "15,200",
                "saturation": "High",
                "satColor": "red",
                "desc": "Fast-paced unboxing of sub-$10 tech items.",
                "hook": "I bought the weirdest $5 gadgets so you don't have to.",
                "arbitrage": "🔥 Arbitrage Alert: High potential on YT Shorts"
            },
            {
                "type": "niche",
                "title": "AI Productivity Tools for Students",
                "platform": "yt",
                "platformLabel": "YouTube",
                "rpm": "$14.50",
                "saturation": "Low",
                "satColor": "green",
                "desc": "Tutorials on using AI to summarize lectures and write essays.",
                "hook": "Stop studying harder. This AI tool does 90% of the work...",
                "arbitrage": False
            }
        ]
        
        output_file = "trends_data.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(scraped_data, f, indent=4, ensure_ascii=False)
            
        print(f"Éxito: Archivo '{output_file}' generado correctamente.")
        
    except Exception as e:
        print(f"Error crítico: {e}")

if __name__ == "__main__":
    fetch_viral_trends()
