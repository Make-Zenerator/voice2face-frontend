<script>
  import SocialProperty1Github from "../../components/image/SocialProperty1Github.svelte";
  import Header from "../../components/header/header_login.svelte";
  import HeaderNon from "../../components/header/header_non.svelte";

  import { onMount } from 'svelte';

  let token = null;
  let isLoggedIn = false;

  function checkSession() {
    console.log('세션 토큰 확인 중...');
    token = sessionStorage.getItem('auth_token');
    console.log('토큰:', token);
    if (!token) {
      isLoggedIn = false;
    } else {
      isLoggedIn = true;
    }
  }

  onMount(() => {
    checkSession();
  });
</script>

<style>
.frame { /* 전체 프레임 영역*/ 
  align-items: center;
  background-color: #fff;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  position: relative;
}

.main-container { /* 디자인 영역 */
  top: 150px;
  align-items: center;
  display: flex;
  flex-direction: column;
  gap: 50px;
  padding: 0px 0px 120px 0px;
  position: relative;
  width: 1200px;
}

.title {
  color: #000000;
  text-align: center;
  font-family: var(--title-large-font-family, 'DmSans-Bold', sans-serif);
  font-size: var(--title-large-font-size, 60px);
  line-height: var(--title-large-line-height, 76px);
  font-weight: var(--title-large-font-weight, 700);
  position: relative;
  width: 412px;
  height: 62px;
}

.subtitle {
  color: #8c8686;
  text-align: center;
  font-family: var(--body-large-font-family, 'DmSans-Regular', sans-serif);
  font-size: var(--body-large-font-size, 20px);
  line-height: var(--body-large-line-height, 32px);
  font-weight: var(--body-large-font-weight, 400);
  position: relative;
  width: 612px;
}

.members-title {
  color: #000000;
  text-align: center;
  font-family: var(--title-large-font-family, 'DmSans-Bold', sans-serif);
  font-size: var(--title-large-font-size, 50px);
  line-height: var(--title-large-line-height, 76px);
  font-weight: var(--title-large-font-weight, 700);
  position: relative;
  width: 412px;
  height: 62px;
}

.members-container {
  display: flex;
  flex-direction: column;
  gap: 54px;
  align-items: center;
  justify-content: flex-start;
  flex-shrink: 0;
  position: relative;
}

.member-row {
  display: flex;
  flex-direction: row;
  gap: 10px;
  align-items: flex-start;
  justify-content: flex-start;
  flex-shrink: 0;
  position: relative;
}

.member-column {
  display: flex;
  flex-direction: column;
  gap: 21px;
  align-items: center;
  justify-content: flex-start;
  flex-shrink: 0;
  position: relative;
}

.member-name {
  color: #000000;
  text-align: center;
  font-family: 'DmSans-Bold', sans-serif;
  font-size: 30px;
  line-height: 40px;
  font-weight: 700;
  position: relative;
  width: 294px;
  height: 40px;
}

.member-image {
  width: 230px;
  height: 230px;
  object-fit: cover;
  border: 1px solid #ccc;
}

.kimhaeji-margin {
  margin-top: 0px;
}

@media (max-width: 894px) {
  .main-container {
    width: 100%;
    padding: 0 10px;
    padding-bottom: 50px;
  }


  .member-row {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
  }

  .member-column {
    width: calc(33.33% - 20px); /* Width minus gap to fit 3 per row */
    box-sizing: border-box;
  }

}

@media (max-width: 763px) {
  .main-container {
    width: 100%;
    padding: 0 10px;
    padding-bottom: 50px;
  }


  .members-container {
    gap: 20px;
  }

  .member-row {
    flex-direction: column;
    align-items: center;
    gap: 45px;
  }

  .member-column {
    width: 100%;
  }

  .kimhaeji-margin {
  margin-top: 30px;
  }
}

@media(max-width: 420px) {
  .main-container {
    top: 100px;
    width: 100%;
    padding: 0 10px;
    gap: 20px;
    padding-bottom: 50px;
  }
  
  .title, .members-title {
    font-size: 36px;
    width: 100%;
    height: auto;
  }

  .subtitle {
    font-size: 16px;
    width: 100%;
    line-height: 24px;
  }

  .members-container {
    gap: 20px;
  }

  .member-row {
    flex-direction: column;
    align-items: center;
    gap: 45px;
  }

  .member-name {
    font-size: 24px;
    width: auto;
  }

  .member-column {
    gap: 10px;
  }

  .members-title {
    margin-top: 20px;
  }
}
</style>

<div class="frame">
  <div class="main-container">
    {#if isLoggedIn}
      <Header />
    {:else}
      <HeaderNon />
    {/if}

    <div class="title">
      About Us
    </div>
    <div class="subtitle">
      안녕하세요! <br>
      사용자의 목소리를 기반으로 가상의 얼굴을 생성하는 서비스,<br>
      Voice2Face를 개발 중인 Make Zenerator 팀입니다. <br>
      (문의&불편사항: mz140103@gmail.com)<br>
    </div>
    <img src="/logo/MZ_aboutus.jpg" alt="MZ_members">
    <div></div>
    <div class="members-title">
      MZ Members
    </div>

    <div class="members-container">
      <div class="member-row">
        <div class="member-column">
          <div>
            <div class="member-name">신호준</div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0" targetPath="https://github.com/internationalwe/"></SocialProperty1Github>
          <img src="https://make-generator.s3.ap-northeast-2.amazonaws.com/profiles/hojun.jpg" class="member-image" alt="신호준">
        </div>
        <div class="member-column">
          <div>
            <div class="member-name">김태양</div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0" targetPath="https://github.com/taeyang916"></SocialProperty1Github>
          <img src="https://make-generator.s3.ap-northeast-2.amazonaws.com/profiles/taeyang.jpg" class="member-image" alt="김태양">
        </div>
        <div class="member-column">
          <div>
            <div class="member-name">정소윤</div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0" targetPath="https://github.com/soyoonjeong"></SocialProperty1Github>
          <img src="https://make-generator.s3.ap-northeast-2.amazonaws.com/profiles/soyoon.jpg" class="member-image" alt="정소윤">
        </div>
      </div>
      <div class="member-row">
        <div class="member-column  kimhaeji-margin">
          <div>
            <div class="member-name">김혜지</div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0" targetPath="https://github.com/carboxaminoo"></SocialProperty1Github>
          <img src="https://make-generator.s3.ap-northeast-2.amazonaws.com/profiles/haeji.jpg" class="member-image" alt="김혜지">
        </div>
        <div class="member-column">
          <div>
            <div class="member-name">임서현</div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0" targetPath="https://github.com/dlatjgus0612"></SocialProperty1Github>
          <img src="https://make-generator.s3.ap-northeast-2.amazonaws.com/profiles/seohyun.jpg" class="member-image" alt="임서현">
        </div>
        <div class="member-column">
          <div>
            <div class="member-name">성주희</div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0" targetPath="https://github.com/jouhy"></SocialProperty1Github>
          <img src="https://make-generator.s3.ap-northeast-2.amazonaws.com/profiles/juhy.jpg" class="member-image" alt="성주희">
        </div>
      </div>

    </div>
  </div>
</div>
