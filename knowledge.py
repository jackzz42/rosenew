import sqlite3

def init_db():
    conn = sqlite3.connect("rosee_knowledge.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS knowledge (topic TEXT, content TEXT)")
    conn.commit()
    conn.close()

def add_knowledge(topic, content):
    conn = sqlite3.connect("rosee_knowledge.db")
    c = conn.cursor()
    c.execute("INSERT INTO knowledge VALUES (?, ?)", (topic.lower(), content))
    conn.commit()
    conn.close()

def get_knowledge(topic):
    conn = sqlite3.connect("rosee_knowledge.db")
    c = conn.cursor()
    c.execute("SELECT content FROM knowledge WHERE topic=?", (topic.lower(),))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None
