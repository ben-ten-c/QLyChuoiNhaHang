# Import class cha NhanVien
# Lưu ý: Cần đảm bảo thư mục gốc dự án nằm trong PYTHONPATH hoặc chạy từ main.py
from src.models.hr.nhan_vien import NhanVien

class QuanLy(NhanVien):
    """
    Class QuanLy (Quản Lý) - Kế thừa từ NhanVien.
    Đặc điểm:
    - Có hệ số trách nhiệm.
    - Lương tính theo công thức khác nhân viên thường.
    - Có quyền duyệt chi tiêu và báo cáo.
    """

    def __init__(self, ma_nhan_vien: str, ho_ten: str, luong_co_ban: float, he_so_trach_nhiem: float):
        # 1. Gọi Constructor của lớp cha (NhanVien)
        # Truyền cứng chức vụ là "Quản Lý"
        super().__init__(ma_nhan_vien, ho_ten, "Quản Lý", luong_co_ban)
        
        # 2. Khởi tạo thuộc tính riêng của Quản Lý (Map với sơ đồ UML)
        self._he_so_trach_nhiem = he_so_trach_nhiem
        self._doanh_so_chi_nhanh = 0.0 # Doanh số quản lý được, dùng để tính thưởng

    # --- GETTER / SETTER RIÊNG ---
    @property
    def doanh_so_chi_nhanh(self):
        return self._doanh_so_chi_nhanh

    @doanh_so_chi_nhanh.setter
    def doanh_so_chi_nhanh(self, doanh_so: float):
        if doanh_so < 0:
            print("Cảnh báo: Doanh số không thể âm.")
        else:
            self._doanh_so_chi_nhanh = doanh_so

    # --- TRIỂN KHAI PHƯƠNG THỨC TRỪU TƯỢNG (POLYMORPHISM) ---
    # BẮT BUỘC phải viết hàm này, nếu không Python sẽ báo lỗi
    def linh_luong(self) -> float:
        """
        Cách tính lương Quản lý:
        = (Lương cơ bản * Hệ số trách nhiệm) + (1% Doanh số chi nhánh)
        """
        luong_cung = self._luong_co_ban * self._he_so_trach_nhiem
        hoa_hong = self._doanh_so_chi_nhanh * 0.01 # Thưởng 1% doanh số
        tong_luong = luong_cung + hoa_hong
        return tong_luong

    # --- CÁC PHƯƠNG THỨC ĐẶC THÙ (CHỈ QUẢN LÝ MỚI CÓ) ---
    
    def duyet_chi_tieu(self, so_tien: float, ly_do: str):
        """Mô phỏng hành động duyệt chi tiền của nhà hàng"""
        print(f"--> [ADMIN] Quản lý {self._ho_ten} đã duyệt chi: {so_tien:,.0f} VND")
        print(f"--> Lý do: {ly_do}")

    def bao_cao_ve_tru_so(self):
        """Mô phỏng báo cáo doanh thu về Chuỗi nhà hàng (Headquarters)"""
        print(f"--> [REPORT] Gửi báo cáo về trụ sở: Chi nhánh hiện tại đạt doanh số {self._doanh_so_chi_nhanh:,.0f} VND")

    # Override lại hàm lay_thong_tin_co_ban để thêm thông tin hệ số
    def lay_thong_tin_co_ban(self) -> str:
        thong_tin_goc = super().lay_thong_tin_co_ban()
        return f"{thong_tin_goc} | Hệ số TN: {self._he_so_trach_nhiem}"