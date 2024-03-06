<script>
  import ButtonStyleFilled from "../../components/button/basic_filled.svelte";
  import MovingFilled from "../../components/button/moving_filled.svelte";
  import Header from "../../components/header_login.svelte";
  let className = "";
  export { className as class };
  export let style;
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox} from 'flowbite-svelte';

 
  let items = [
    { id: 1, request_date: 'Toyota', end_date: 'ABC', result_gender: 1 , result_age:1, make:1, result_audio: "url"},
  
  ];
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
        width: 1500px;
        font-size: 14pt;
        <!-- height: 120px; -->
        <!-- position: relative; -->
        <!-- object-fit: cover; -->
        <!-- margin-left: auto; -->
        <!-- margin-right: auto; -->
    ">
    <TableHead>
      <TableHeadCell style="width:150px; font-size:14pt;">요청 순서</TableHeadCell>
      <TableHeadCell style="width:150px; font-size:14pt;">요청 시간</TableHeadCell>
      <TableHeadCell style="width:150px; font-size:14pt;">완료 시간</TableHeadCell>
      <TableHeadCell style="width:100px; font-size:14pt;">성별</TableHeadCell>
      <TableHeadCell style="width:100px; font-size:14pt;">나이</TableHeadCell>
      <TableHeadCell style="width:150px; font-size:14pt;">진행 상태</TableHeadCell>
      <TableHeadCell style="width:100px; font-size:14pt;">목소리 듣기</TableHeadCell>
      <TableHeadCell style="width:20%; font-size:14pt;">결과 보기</TableHeadCell>
      <TableHeadCell>
        <span class="sr-only">Edit</span>
      </TableHeadCell>
    </TableHead>
    <TableBody class="divide-y">
      {#each items as item}
        <TableBodyRow>
          <TableBodyCell>{item.id}</TableBodyCell>
          <TableBodyCell>{item.request_date}</TableBodyCell>
          <TableBodyCell>{item.end_date}</TableBodyCell>
          <TableBodyCell>{item.result_gender}</TableBodyCell>
          <TableBodyCell>{item.result_age}</TableBodyCell>

          <TableBodyCell>
            {#if item.make == 0}<img src = "/resultlist/생성중.png" style="width: 100%; height: 45%; max-width: 100%; max-height: 100%; " alt="생성 중"/>
            {:else if item.make == 1}<img src = "/resultlist/생성완료.png" style="width: 100%; height: 45%; max-width: 100%; max-height: 100%;" alt="생성 완료"/>
            {:else if item.make == 2}<img src = "/resultlist/생성실패.png "style="width: 100%; height: 45%; max-width: 100%; max-height: 100%;" alt="생성 실패"/>
            {/if}
          </TableBodyCell>
          <TableBodyCell>
              <audio src={`/a4d0-472e-bb6d-d11ccac43e21`} controls></audio>
            </TableBodyCell>
          <TableBodyCell>
            {#if item.make ==1}
              <MovingFilled targetPath='/result' name="결과 확인"> </MovingFilled>
            {:else if item.make ==2}
              Error
              {/if}
            </TableBodyCell>
        </TableBodyRow>
          {/each}
    </TableBody>
  </Table>
</div>


