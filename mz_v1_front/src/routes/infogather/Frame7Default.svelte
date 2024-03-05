<script>
  export let unknownProp69 = "default";
  let className = "";
  export { className as class };
  export let style;
  export let audioUrl;
  const variantsClassName = "unknown-prop-69-" + unknownProp69;
  $: if (audioUrl) {
    const audio = new Audio(audioUrl);
    audio.play().catch(error => console.error('오디오 재생 실패:', error));
  }
</script>
<img
  class="{'frame-7-default ' + className + ' ' + variantsClassName}"
  style="{' display: flex; flex-direction: row; gap: 10px; align-items: flex-start; justify-content: flex-start; flex-shrink: 0;height: auto; position: relative; overflow: visible;' + style}"
  src="/join/frame-7-default.svg"
/>
