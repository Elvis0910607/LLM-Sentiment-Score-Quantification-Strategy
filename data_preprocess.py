import pandas as pd
import numpy as np
emotion = pd.read_csv("C:/Users/r0982/OneDrive/桌面/LLM Stock Analysis/train_stockemo.csv")
emotion
emotion_2col = emotion[["emo_label", "processed"]]
emotion_2col['instruction'] = "Based on the following sentences or news, please help me calculate the positive sentiment score of the sentence"

emotion_mapping = {
    "confusion": 1,
    "anxiety": 2,
    "panic": 3,
    "disgust": 4,
    "depression": 5,
    "anger": 6,
    "amusement": 7,
    "optimism": 8,
    "belief": 9,
    "surprise": 10,
    "ambiguous": 11,
    "excitement": 12
}
emotion_2col["emo_label_score"] = emotion_2col["emo_label"].map(emotion_mapping)

data = []

for _, row in emotion_2col.iterrows():
    conversation = {
        "conversations": [
            {"role": "system", "content": row['instruction']},
            {"role": "user", "content": row['processed']},
            {"role": "assistant", "content": str(row['emo_label_score'])}  
        ]
    }
    data.append(conversation)

with open("formatted_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)