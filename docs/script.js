const API_URL = "https://chaos-fairytale-api.onrender.com/generate_story"; // Render のURLを設定

document.getElementById("generate").addEventListener("click", async function() {
    const keyword = document.getElementById("keyword").value.trim();
    const storyDiv = document.getElementById("story");

    if (keyword === "") {
        storyDiv.innerHTML = "<p style='color:red;'>単語を入力してください！</p>";
        return;
    }

    storyDiv.innerHTML = "<p>昔話を生成中...</p>";

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt: keyword })
        });
        console.log(response);

        const data = await response.json();
        storyDiv.innerHTML = `<p>${data.story}</p>`;
    } catch (error) {
        storyDiv.innerHTML = "<p style='color:red;'>エラーが発生しました。</p>";
        console.error(error);
    }
});
