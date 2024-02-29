<script>
    import ButtonStyleFilled from "../routes/join/ButtonStyleFilled.svelte";
    let className = "";
    export { className as class };
    export let style;

    
  </script>
<style global>
     a {
    text-decoration: none;
  }
</style>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Titan+One&display=swap" rel="stylesheet">


<div
  style="
    background: var(--neutral-0, #ffffff);
    border-style: solid;
    border-color: var(--neutral-2, #dee5ed);
    border-width: 0px 0px 1px 0px;
    padding: 8px 98px 8px 98px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    flex-shrink: 0;
    width: 1440px;
    height: 72px;
    position: relative;
    overflow: hidden;
  "
>
  <div style="flex-shrink: 0; width: 299px; height: 55px; position: static">
    <a href="/">
      <div
      style="
      color: var(--7b95b7, #6b6b6b);
      text-align: left;
      font-family: 'Titan One', sans-serif;
      font-style: normal;
      line-height: 24px;
      font-weight: 400;
      font-size: 26px;
      position: absolute;
      left: 188px;
      top: 31px;
    "
      >
        Make Zenerator
      </div>
      <img href="/"
        class="{'image-2 ' + className}"
        style="
      width: 90px;
      height: 55px;
      position: absolute;
      left: 98px;
      top: 8.5px;
      object-fit: cover;
    "
        src="/join/image-20.png"
        alt="logo"
      /></a>
  </div>
  <div
    style="
      display: flex;
      flex-direction: row;
      gap: 48px;
      align-items: center;
      justify-content: flex-start;
      flex-shrink: 0;
      position: relative;
    "
  >
    <a href="aboutus_non"
    style="
    color: var(--7b95b7, #6b6b6b);
    text-align: center;
    font-family: var(
      --body-small-font-family,
      'DmSans-Regular',
      sans-serif
    );
    font-size: var(--body-small-font-size, 24px);
    line-height: var(--body-small-line-height, 24px);
    font-weight: var(--body-small-font-weight, 400);
    position: relative;
  "
>
      About us
</a>
    <a href="/login" 
    style="
    color: var(--7b95b7, #6b6b6b);
    text-align: center;
    font-family: var(
      --body-small-font-family,
      'DmSans-Regular',
      sans-serif
    );
    font-size: var(--body-small-font-size, 24px);
    line-height: var(--body-small-line-height, 24px);
    font-weight: var(--body-small-font-weight, 400);
    position: relative;
  "
>
      로그인  
</a>
    <ButtonStyleFilled
      styleVariant="filled"
      style="
        background: var(--6b6b6b, #000000);
        border-color: var(--7b95b7, #6b6b6b);
        flex-shrink: 0;
      "
      name ="회원가입"
      targetPath="/join"
    ></ButtonStyleFilled>
  </div>
</div>