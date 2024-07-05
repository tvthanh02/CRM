const btn = document.querySelector(".btn-main");
const dialog = document.querySelector(".dialog");
const btnOk = document.querySelector(".btn-ok");
const btnCancel = document.querySelector(".btn-cancel");
const dialogText = document.querySelector(".dialog-text");
const content = document.querySelector(".content");

const setStatusDialog = () => {
  let title = "Hiện tại không còn cơ hội nào";
  let isActiveBtnOk = false;
  const random = Math.floor(Math.random() * 100);
  if (random > 60) {
    dialogText.style.color = "black";
    title = "Bạn có chắn chắn muốn nhận cơ hội này";
    isActiveBtnOk = true;
  } else {
    dialogText.style.color = "red";
  }

  dialogText.innerHTML = title;
  isActiveBtnOk
    ? (btnOk.style.display = "block")
    : (btnOk.style.display = "none");
};

const customers = [
  {
    stt: 1,
    name: "Triệu Văn Thành",
    address: "Hoàng Mai, Hà Nội",
    phone: "03257539556",
    vip: "có",
  },
  {
    stt: 2,
    name: "Hoàng Thu Lan",
    address: "32 Đình Thôn, Mỹ Đình 2, Hà Nội",
    phone: "03456475823",
    vip: "không",
  },
  {
    stt: 3,
    name: "Ngô Bá Khá",
    address: "Từ Sơn, Berlin",
    phone: "0333444777",
    vip: "vvip",
  },
  {
    stt: 4,
    name: "Nguyễn Mạnh Dũng",
    address: "Thanh Ba, Phú Thọ",
    phone: "079856443",
    vip: "không",
  },
];

btn.addEventListener("click", () => {
  setStatusDialog();
  dialog.classList.add("open");
});

const handleOK = () => {
  const data = customers[Math.floor(Math.random() * 4)];
  let html = `
 <div class="item">
          <p>${data.stt}</p>
          <p>${data.name}</p>
          <p>${data.address}</p>
           <p>${data.phone}</p>
          <p>
          ${data.vip}
          </p>
        </div>
 `;

  content.insertAdjacentHTML("beforeend", html);
};

btnCancel.addEventListener("click", () => dialog.classList.remove("open"));

btnOk.addEventListener("click", () => {
  dialog.classList.remove("open");
  handleOK();
});
