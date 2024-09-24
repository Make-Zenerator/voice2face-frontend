<script>
    let className = "";
    export { className as class };
    export let style;
    export let src = 'logo/login_image.webp'
  //   export let targetPath = "/";
  // function handleClick() {
  //   goto(targetPath); // 버튼 클릭 시 targetPath로 이동
  // }
  </script>
  <img
    class="{'placeholder-image ' + className}"
    style="{'border-radius: 24px;padding: 10px; display: flex; flex-direction: row; gap: 10px; align-items: center; justify-content: center; align-self: stretch;flex: 1;height: auto; position: relative; overflow: visible;' + style}"
    src={src}
    alt="login_image"
  />