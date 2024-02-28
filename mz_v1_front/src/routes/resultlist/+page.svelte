<script>
  import ButtonStyleFilled from "./ButtonStyleFilled.svelte";
  let className = "";
  export { className as class };
  export let style;
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox} from 'flowbite-svelte';

  let items = [
    { id: 1, maker: 'Toyota', type: 'ABC', make: 1 },
    { id: 2, maker: 'Ford', type: 'CDE', make: 2 },
    { id: 3, maker: 'Volvo', type: 'FGH', make: 3 },
    { id: 4, maker: 'Saab', type: 'IJK', make: 1 }
  ];
  </script>
<div
style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 120px 0px; display: flex; flex-direction: column; gap: 30px; align-items: center; justify-content: flex-start; height: 845px; position: relative; ' + style}"
>
<div>
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
      position: relative;
      overflow: hidden;
    "
  >
  <div style="flex-shrink: 0; width: 299px; height: 55px; position: static">
    <div
      style="
        color: var(--7b95b7, #6b6b6b);
        text-align: left;
        font-family: 'TitanOne-Regular', sans-serif;
        font-size: 24px;
        line-height: 24px;
        font-weight: 400;
        position: absolute;
        left: 188px;
        top: 30.5px;
      "
    >
      Make Zenerator
    </div>
      <img
        class="{'image-2 ' + className}"
        style="
          width: 90px;
          height: 55px;
          position: absolute;
          left: 98px;
          top: 8px;
          object-fit: cover;
        "
        src="/resultlist/image-20.png"
      />
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
      <div
        style="
          color: var(--7b95b7, #6b6b6b);
          text-align: center;
          font-family: var(
            --body-small-font-family,
            'DmSans-Regular',
            sans-serif
          );
          font-size: var(--body-small-font-size, 16px);
          line-height: var(--body-small-line-height, 24px);
          font-weight: var(--body-small-font-weight, 400);
          position: relative;
        "
      >
        About us
      </div>
      <div
        style="
          color: var(--7b95b7, #6b6b6b);
          text-align: center;
          font-family: var(
            --body-small-font-family,
            'DmSans-Regular',
            sans-serif
          );
          font-size: var(--body-small-font-size, 16px);
          line-height: var(--body-small-line-height, 24px);
          font-weight: var(--body-small-font-weight, 400);
          position: relative;
        "
      >
        로그아웃
      </div>
      <ButtonStyleFilled
        styleVariant="filled"
        style="
          background: var(--6b6b6b, #000000);
          border-color: var(--7b95b7, #6b6b6b);
          flex-shrink: 0;
        "
      ></ButtonStyleFilled>
    </div>
  </div>
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
        <!-- height: 120px; -->
        <!-- position: relative;
        <!-- object-fit: cover; -->
        <!-- margin-left: auto; -->
        <!-- margin-right: auto; -->
    ">
    <TableHead>
      <TableHeadCell>요청 순서</TableHeadCell>
      <TableHeadCell>요청 시간</TableHeadCell>
      <TableHeadCell>완료 시간</TableHeadCell>
      <TableHeadCell>성별</TableHeadCell>
      <TableHeadCell>나이</TableHeadCell>
      <TableHeadCell>진행 상태</TableHeadCell>
      <TableHeadCell>목소리 듣기</TableHeadCell>
      <TableHeadCell>결과 보기</TableHeadCell>
      <TableHeadCell>
        <span class="sr-only">Edit</span>
      </TableHeadCell>
    </TableHead>
    <TableBody class="divide-y">
      {#each items as item}
        <TableBodyRow>
          <TableBodyCell>{item.id}</TableBodyCell>
          <TableBodyCell>{item.maker}</TableBodyCell>
          <TableBodyCell>{item.type}</TableBodyCell>
          <TableBodyCell>{item.make}</TableBodyCell>
          <TableBodyCell>{item.make}</TableBodyCell>
          <TableBodyCell>
            {#if item.make == 0}<img src = "/resultlist/생성중.png" style="width: 35%; height: 45%; max-width: 100%; max-height: 100%;" alt="생성 중"/>
            {:else if item.make == 1}<img src = "/resultlist/생성완료.png" style="width: 35%; height: 45%; max-width: 100%; max-height: 100%;" alt="생성 중"/>
            {:else if item.make == 2}<img src = "/resultlist/생성실패.png "style="width: 35%; height: 45%; max-width: 100%; max-height: 100%;" alt="생성 중"/>
            {/if}
          </TableBodyCell>
          <TableBodyCell>
            <!-- <input type="button"
              src="/resultlist/Frame_7.png"/> -->
              <audio src="sound.mp3" autoplay loop controls id="myAudio"></audio>
            </TableBodyCell>
          <TableBodyCell>

          </TableBodyCell>
        </TableBodyRow>
          {/each}
    </TableBody>
  </Table>
</div>