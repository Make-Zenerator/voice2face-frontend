<script>
  export let styleVariant = "outlined";
  let className = "";
  export { className as class };
  export let style;
  const variantsClassName = "style-variant-" + styleVariant;
</script>
<div
  style="{'background: var(--neutral-10, #486284);border-radius: 50px; border-style: solid; border-color: var(--neutral-10, #486284); border-width: 1px; padding: 12px 20px 12px 20px; display: flex; flex-direction: row; gap: 10px; align-items: center; justify-content: center; position: relative; overflow: hidden;' + style}"
>
  <div
    style="
      color: var(--neutral-0, #ffffff);
      text-align: left;
      font-family: var(--body-small-font-family, 'DmSans-Regular', sans-serif);
      font-size: var(--body-small-font-size, 16px);
      line-height: var(--body-small-line-height, 24px);
      font-weight: var(--body-small-font-weight, 400);
      position: relative;
    "
  >
    Do something
  </div>
</div>
