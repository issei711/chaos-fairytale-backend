document.getElementById("generate").addEventListener("click", async function() {
    const keyword = document.getElementById("keyword").value.trim();
    const storyDiv = document.getElementById("story");

    if (keyword === "") {
        storyDiv.innerHTML = "<p style='color:red;'>単語を入力してください！</p>";
        return;
    }

    storyDiv.innerHTML = "<p>昔話を生成中...</p>";

    try {
        const response = await fetch("https://chaos-fairytale-api.onrender.com/generate_story", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ keyword: keyword })
        });

        const data = await response.json();
        storyDiv.innerHTML = `<p>${data.story}</p>`;
    } catch (error) {
        storyDiv.innerHTML = "<p style='color:red;'>エラーが発生しました。</p>";
        console.error(error);
    }
});
