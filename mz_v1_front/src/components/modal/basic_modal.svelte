<script>
	export let showModal; // boolean
	export let p_header = "주의사항";

	let dialog; // HTMLDialogElement

	$: if (dialog && showModal) dialog.showModal();
</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-noninteractive-element-interactions -->
<dialog
	bind:this={dialog}
	on:close={() => (showModal = false)}
	on:click|self={() => dialog.close()}
>
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div class="modal-content" on:click|stopPropagation>
		<p class="header">
			<strong>{p_header}</strong>
		</p>
		<hr />
		<slot />
		<hr />
		<!-- svelte-ignore a11y-autofocus -->
		<button  class="close-button" autofocus on:click={() => dialog.close()}>닫기</button>
	</div>
</dialog>

<style>
	dialog {
		max-width: 32em;
		border-radius: 0.2em;
		border: none;
		padding: 0;
	}

	dialog::backdrop {
		background: rgba(0, 0, 0, 0.3);
	}

	dialog > div {
		padding: 1em;
	}

	dialog[open] {
		animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
	}

    @media(max-width: 420px) {
        dialog {
		max-width: 365px;
		
	}
  }

	@keyframes zoom {
		from {
			transform: scale(0.95);
		}
		to {
			transform: scale(1);
		}
	}

	dialog[open]::backdrop {
		animation: fade 0.2s ease-out;
	}

	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}

	.modal-content {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 5px;
		padding: 10px;
        padding-right: 30px;
        padding-left: 30px;
	}

	.header {
		font-size: 24pt;
	}

	button {
		display: block;
	}

    .close-button {
		width: 100%;
        height: 40px;
		border: none;
		background: none;
		cursor: pointer;
		transition: background-color 0.3s, color 0.3s;
	}

	.close-button:hover {
		background-color: #e0e0e0;
		color: #333;
	}

	hr {
		width: 100%; /* hr의 너비를 부모 요소의 전체 너비로 설정 */
	}


    

</style>