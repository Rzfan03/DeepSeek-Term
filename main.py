from openai import OpenAI
import pyfiglet

banner = pyfiglet.figlet_format("DeepSeek Term")
print(banner)
print(f'DeepSeek in your terminal!')
print("my github : https://github.com/Rzfan03")



client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="GANTI DENGAN API MU",
)


stop_words = ["no"]

print("Hai! Ada yang bisa aku bantu? (Ketik 'no' untuk berhenti)")


while True:
    user_input = input("Anda: ").strip().lower()
    

    if any(word in user_input for word in stop_words):
        print("Terima kasih telah menggunakan layanan ini. Sampai jumpa!")
        break
    

    if not user_input:
        print("Silakan masukkan pertanyaan Anda.")
        continue
    

    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://localhost",
                "X-Title": "DeepSeek Chat",
            },
            extra_body={},
            model="deepseek/deepseek-r1-distill-llama-70b:free",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )
        
        
        print("DeepSeek: " + completion.choices[0].message.content)
        print()  
        
    except Exception as e:
        print(f"Error!: {e}")
        print("Error!")
