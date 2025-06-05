from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="mydb",
        user="postgres",
        password="yourpassword"
    )

@app.route("/query", methods=["POST"])
def query():
    sql = request.form.get("sql")
    if not sql:
        return jsonify({"error": "SQL yok"}), 400
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        if cur.description:
            rows = cur.fetchall()
            result = [list(row) for row in rows]
        else:
            conn.commit()
            result = {"status": "OK"}
        cur.close()
        conn.close()
    except Exception as e:
        result = {"error": str(e)}
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
