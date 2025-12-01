from abc import ABC, abstractmethod
from datetime import datetime

class NhanVien(ABC):
    """
    Lớp trừu tượng NhanVien.
    Đại diện cho tất cả nhân sự trong nhà hàng.
    Không thể khởi tạo trực tiếp (Instance) mà phải thông qua các lớp con.
    """

    def __init__(self, ma_nhan_vien: str, ho_ten: str, chuc_vu: str, luong_co_ban: float):
        # Sử dụng dấu gạch dưới (_) để thể hiện thuộc tính Protected (# trong UML)
        # Các lớp con (QuanLy, PhucVu...) có thể truy cập trực tiếp các biến này.
        self._ma_nhan_vien = ma_nhan_vien
        self._ho_ten = ho_ten
        self._chuc_vu = chuc_vu
        self._luong_co_ban = luong_co_ban
        
        # Tự động gán ngày vào làm là thời điểm tạo đối tượng (hoặc có thể truyền vào)
        self._ngay_vao_lam = datetime.now()
        
        # Thuộc tính hỗ trợ tính lương (số ngày đi làm)
        self._so_ngay_cong = 0

    # --- ENCAPSULATION (TÍNH ĐÓNG GÓI) ---
    # Sử dụng @property để tạo Getter/Setter an toàn
    
    @property
    def ho_ten(self):
        return self._ho_ten

    @property
    def ma_nhan_vien(self):
        return self._ma_nhan_vien

    @property
    def chuc_vu(self):
        return self._chuc_vu

    @property
    def luong_co_ban(self):
        return self._luong_co_ban

    @luong_co_ban.setter
    def luong_co_ban(self, luong_moi: float):
        if luong_moi < 0:
            raise ValueError("Lương cơ bản không thể âm!")
        self._luong_co_ban = luong_moi

    # --- COMMON METHODS (PHƯƠNG THỨC CHUNG) ---
    
    def cham_cong(self):
        """
        Ghi nhận 1 ngày công làm việc.
        Hàm này dùng chung cho tất cả nhân viên.
        """
        self._so_ngay_cong += 1
        print(f"Đã chấm công cho {self._ho_ten}. Tổng ngày công: {self._so_ngay_cong}")

    def lay_thong_tin_co_ban(self) -> str:
        """Trả về chuỗi thông tin định dạng để in ấn"""
        ngay_str = self._ngay_vao_lam.strftime("%d/%m/%Y")
        luong_str = "{:,.0f}".format(self._luong_co_ban) # Format 1,000,000
        return f"Mã: {self._ma_nhan_vien} | Tên: {self._ho_ten} | Chức vụ: {self._chuc_vu} | Lương CB: {luong_str} VND | Ngày vào: {ngay_str}"

    # --- ABSTRACTION (TÍNH TRỪU TƯỢNG) ---
    
    @abstractmethod
    def linh_luong(self) -> float:
        """
        Phương thức trừu tượng tính lương thực lĩnh.
        Bắt buộc các lớp con (QuanLy, DauBep, PhucVu) phải định nghĩa lại (Override).
        """
        pass
    
 