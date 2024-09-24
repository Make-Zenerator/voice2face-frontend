  <style>
    :root {
      --neutral-0: #ffffff;
      --body-large-font-family: 'DmSans-Regular', sans-serif;
      --body-large-font-size: 20px;
      --body-large-line-height: 50px;
      --body-large-font-weight: 400;
      --title-large-font-family: 'DmSans-Bold', sans-serif;
      --title-large-font-size: 50px;
      --title-large-line-height: 76px;
      --title-large-font-weight: 700;
      --color-6b6b6b: #000000;
      --color-8c8686: #8c8686;
    }
  
    .container {
      background: var(--neutral-0);
      padding: 160px 0px 120px 0px;
      display: flex;
      flex-direction: column;
      gap: 70px;
      align-items: center;
      justify-content: flex-start;
      min-height: 100vh;
      position: relative;
    }
  
    .image-22 {
      flex-shrink: 0;
      width: 320px;
      position: relative;
      object-fit: cover;
      margin-left: auto;
      margin-right: auto;
    }
  
    .maintenance-text {
      color: var(--color-8c8686);
      text-align: center;
      font-family: var(--body-large-font-family);
      font-size: var(--body-large-font-size);
      line-height: var(--body-large-line-height);
      font-weight: var(--body-large-font-weight);
      position: relative;
      width: 800px;
      margin-left: auto;
      margin-right: auto;
    }
  
    .title {
      color: var(--color-6b6b6b);
      font-family: var(--title-large-font-family);
      font-size: var(--title-large-font-size);
      line-height: var(--title-large-line-height);
      font-weight: var(--title-large-font-weight);
    }
  </style>
  
  <div class="container">
    <div>
      <img
        class="image-22"
        src="./logo/maintenance.png"
        alt="maintenance"
      />
      <div class="maintenance-text">
        <p class="title">현재 페이지를 업데이트 중입니다!</p>
        <p>불편을 드려 죄송합니다. 조금만 기다려 주세요.</p>
      </div>
    </div>
  </div>
  