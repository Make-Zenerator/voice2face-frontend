<script>
  import ButtonStyleFilled from "../../routes/join/ButtonStyleFilled.svelte";
  let className = "";
  export { className as class };
  export let style;
</script>

<style>
  .border {
    top: 72px;
    border-style: solid;
    border-color: var(--neutral-2, #dee5ed);
    border-width: 0px 0px 1px 0px;
    width: 1200px;
  }

  .header-container {
    background: var(--neutral-0, #ffffff);
    padding: 8px 80px; 
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    width: 1200px;
    height: 72px;
    overflow: hidden;
  }

  .brand {
    flex-shrink: 0;
    width: 299px;
    height: 55px;
    position: static;
  }

  .brand-logo {
    width: 70px;
    position: absolute;
    left: 100px;
    top: 2px;
    object-fit: cover;
  }

  .brand-name {
    color: var(--7b95b7, #6b6b6b);
    text-align: center;
    font-family: 'yg-jalnan';
    font-size: 20px;
    line-height: 28px;
    font-weight: 400;
    position: absolute;
    left: 170px;
    top: 27px;
  }

  .navigation {
    display: flex;
    flex-direction: row;
    gap: 58.5px;
    align-items: center;
    justify-content: flex-start;
  }

  .nav-link {
    color: var(--7b95b7, #6b6b6b);
    text-align: center;
    font-family: var(--body-small-font-family, 'DmSans-Regular', sans-serif);
    font-size: var(--body-small-font-size, 24px);
    line-height: var(--body-small-line-height, 24px);
    font-weight: var(--body-small-font-weight, 400);
  }
</style>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Titan+One&display=swap" rel="stylesheet">

<div class="border">
  <div class="header-container">
    <div>
      <a href="/" class="brand">
        <div class="brand-name">
          <strong>Make Zenerator</strong>
        </div>
        <img class="brand-logo" src="./logo/logo1.png" alt="logo">
      </a>
    </div>
    <div class="navigation">
      <a href="/aboutus" class="nav-link">About us</a>
      <a href="/login" class="nav-link">로그인</a>
      <ButtonStyleFilled 
          styleVariant="filled" 
          style="
          background: var(--6b6b6b, #000000);
          border-color: var(--7b95b7, #6b6b6b);
          flex-shrink: 0;
        " 
          name="회원가입" 
          targetPath="/join"
        ></ButtonStyleFilled>
    </div>
  </div>
</div>