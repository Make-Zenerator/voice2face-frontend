<script>
  import MovingFilled from "../../components/button/moving_filled.svelte";
  import Header from "../../components/header_login.svelte";
  import { onMount } from 'svelte';
  let className = "";
  export { className as class };
  export let style;
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell} from 'flowbite-svelte';

  let items = [];
  // [id, user_id, age, gender, voice_url, created_at, latest_mz_result_id, statuss, updated_at]

  onMount(async () => {
    const token = sessionStorage.getItem('auth_token'); // sessionStorage에서 토큰 가져오기
    const response = await fetch('http://175.45.194.59:5050/api/v1/mz-request', {
      method: 'GET',
      headers: {
                'Token': token,
      },
    });

    if (response.ok) {
      const data = await response.json();
      items = data.mz_request_list; // 서버로부터 받은 데이터로 items 업데이트
    } else if(response.status === 400) {
      alert("데이터베이스 에러");
    }else {
      console.error('데이터를 가져오는 데 실패했습니다.');
      alert("요청 중 에러가 발생했습니다.")
    }
  });
  </script>



<div
style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 120px 0px; display: flex; flex-direction: column; gap: 30px; align-items: center; justify-content: flex-start; height: 845px; position: relative; ' + style}"
>
<Header></Header>
<div>
  <img
    class="image-22"
    style="
      flex-shrink: 0;
      width: 196px;
      height: 120px;
      position: relative;
      object-fit: cover;
      margin-left: auto;
      margin-right: auto;
    "
    src="/resultlist/image-21.png"
  />
  <div
    style="
      color: #8c8686;
      text-align: center;
      font-family: var(--body-large-font-family, 'DmSans-Regular', sans-serif);
      font-size: var(--body-large-font-size, 20px);
      line-height: var(--body-large-line-height, 32px);
      font-weight: var(--body-large-font-weight, 400);
      position: relative;
      width: 612px;
      margin-left: auto;
      margin-right: auto;
    "
  >
    생성 이미지는 선택 버튼을 통해 확인하실 수 있습니다.
  </div>
</div>

  <Table hoverable={true}
    style="
        flex-shrink: 0;
        width: 1200px;
        font-size: 14pt;
        <!-- height: 120px; -->
        <!-- position: relative; -->
        <!-- object-fit: cover; -->
        <!-- margin-left: auto; -->
        <!-- margin-right: auto; -->
    ">
    <TableHead>
      <TableHeadCell style="width:15%; font-size:14pt;">요청 시간</TableHeadCell>
      <TableHeadCell style="width:15%; font-size:14pt;">완료 시간</TableHeadCell>
      <TableHeadCell style="width: 8%; font-size:14pt;">성별</TableHeadCell>
      <TableHeadCell style="width: 8%; font-size:14pt;">나이</TableHeadCell>
      <TableHeadCell style="width:15%; font-size:14pt;">진행 상태</TableHeadCell>
      <TableHeadCell style="width:8%; font-size:14pt;">목소리 듣기</TableHeadCell>
      <TableHeadCell style="width:5%; font-size:14pt;">결과 보기</TableHeadCell>
      <TableHeadCell>
        <span class="sr-only">Edit</span>
      </TableHeadCell>
    </TableHead>
    <TableBody class="divide-y">
      {#each items as item}
        <TableBodyRow>
          <TableBodyCell>{item.created_at}</TableBodyCell>
          <TableBodyCell>
            {#if item.updated_at != null} {item.updated_at}{/if}
          </TableBodyCell>
          <TableBodyCell>{item.gender}</TableBodyCell>
          <TableBodyCell>{item.age}</TableBodyCell>

          <TableBodyCell>
            {#if item.status == null}<img src = "/resultlist/생성중.png" style="width: 100%; height: 45%; max-width: 100%; max-height: 100%; " alt="생성 중"/>
            {:else if item.status == "Success"}<img src = "/resultlist/생성완료.png" style="width: 100%; height: 45%; max-width: 100%; max-height: 100%;" alt="생성 완료"/>
            {:else}<img src = "/resultlist/생성실패.png "style="width: 100%; height: 45%; max-width: 100%; max-height: 100%;" alt="생성 실패"/>
            {/if}
          </TableBodyCell>
          <TableBodyCell>
              <audio src={item.voice_url} controls></audio>
            </TableBodyCell>
          <TableBodyCell>
            {#if item.status =="Success"}
              <MovingFilled targetPath='/result' name="결과 확인" id = {item.id} latest_id = {item.latest_mz_result_id}> </MovingFilled>
            {:else if item.status == "Failed"}
              Error
              {/if}
            </TableBodyCell>
        </TableBodyRow>
          {/each}
    </TableBody>
  </Table>
</div>


