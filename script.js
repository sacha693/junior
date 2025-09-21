document.addEventListener('DOMContentLoaded', () => {
    // 選擇所有具有 .tool-card 類別的元素
    const toolCards = document.querySelectorAll('.tool-card');

    // 巡迴每一個法寶卡片，並為其添加點擊事件監聽器
    toolCards.forEach(card => {
        card.addEventListener('click', () => {
            // 點擊時切換 .active 類別
            // 如果卡片有 .active，就移除它；如果沒有，就添加它
            card.classList.toggle('active');
        });
    });
});
