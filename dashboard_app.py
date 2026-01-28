import os

import pandas as pd
import psycopg2
import streamlit as st


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5431")),
        dbname=os.getenv("DB_NAME", "postgres"),
        user=os.getenv("DB_USER", "odoo"),
        password=os.getenv("DB_PASSWORD", "odoo"),
    )


@st.cache_data(ttl=60)
def load_dataframe(sql: str) -> pd.DataFrame:
    with get_connection() as conn:
        return pd.read_sql(sql, conn)


st.set_page_config(page_title="Dashboard AI - Chấm công & Lương", layout="wide")

st.title("Dashboard AI (demo) - Chấm công & Lương")
st.caption(
    "Dashboard này đọc trực tiếp từ Postgres (Odoo). "
    "Nếu chưa có dữ liệu, hãy tạo DB Odoo và nhập chấm công/phiếu lương trước."
)

col1, col2, col3 = st.columns(3)
with col1:
    st.text_input("DB_HOST", os.getenv("DB_HOST", "localhost"), disabled=True)
with col2:
    st.text_input("DB_PORT", os.getenv("DB_PORT", "5431"), disabled=True)
with col3:
    st.text_input("DB_NAME", os.getenv("DB_NAME", "postgres"), disabled=True)

st.divider()

st.subheader("1) Tổng quan chấm công")
try:
    bcc = load_dataframe(
        """
        SELECT
            ngay_cham_cong,
            trang_thai,
            tong_gio_lam,
            phut_di_muon,
            phut_ve_som
        FROM bang_cham_cong
        WHERE ngay_cham_cong IS NOT NULL
        ORDER BY ngay_cham_cong DESC
        LIMIT 5000
        """
    )

    if bcc.empty:
        st.info("Chưa có dữ liệu trong bảng `bang_cham_cong`.")
    else:
        bcc["ngay_cham_cong"] = pd.to_datetime(bcc["ngay_cham_cong"]).dt.date

        left, right = st.columns([2, 1])
        with left:
            by_day = (
                bcc.groupby("ngay_cham_cong", as_index=False)
                .agg(
                    tong_gio_lam=("tong_gio_lam", "sum"),
                    phut_di_muon=("phut_di_muon", "sum"),
                    phut_ve_som=("phut_ve_som", "sum"),
                )
                .sort_values("ngay_cham_cong")
            )
            st.line_chart(by_day.set_index("ngay_cham_cong")["tong_gio_lam"], height=260)
            st.bar_chart(by_day.set_index("ngay_cham_cong")[["phut_di_muon", "phut_ve_som"]], height=260)

        with right:
            st.write("Phân bố trạng thái")
            by_status = bcc["trang_thai"].value_counts().rename_axis("trang_thai").reset_index(name="count")
            st.dataframe(by_status, use_container_width=True, hide_index=True)

        st.write("Dữ liệu gần đây")
        st.dataframe(bcc.head(200), use_container_width=True, hide_index=True)
except Exception as exc:
    st.error(
        "Không đọc được dữ liệu chấm công. "
        "Kiểm tra biến môi trường DB_* hoặc đảm bảo DB đã có bảng `bang_cham_cong`."
    )
    st.exception(exc)

st.divider()

st.subheader("2) Tổng quan phiếu lương")
try:
    pl = load_dataframe(
        """
        SELECT
            thang,
            nam,
            thuc_linh,
            tien_phat,
            tong_gio_lam
        FROM hr_phieu_luong
        ORDER BY nam DESC, thang DESC
        LIMIT 5000
        """
    )

    if pl.empty:
        st.info("Chưa có dữ liệu trong bảng `hr_phieu_luong`.")
    else:
        pl["thang"] = pl["thang"].astype(str)
        pl["nam"] = pl["nam"].astype(int)
        pl["ky"] = pl["nam"].astype(str) + "-" + pl["thang"].str.zfill(2)

        by_period = (
            pl.groupby("ky", as_index=False)
            .agg(
                tong_quy_luong=("thuc_linh", "sum"),
                tong_phat=("tien_phat", "sum"),
                tong_gio=("tong_gio_lam", "sum"),
            )
            .sort_values("ky")
        )

        c1, c2 = st.columns(2)
        with c1:
            st.bar_chart(by_period.set_index("ky")["tong_quy_luong"], height=280)
        with c2:
            st.bar_chart(by_period.set_index("ky")["tong_phat"], height=280)

        st.write("Phiếu lương gần đây")
        st.dataframe(pl.head(200), use_container_width=True, hide_index=True)
except Exception as exc:
    st.error(
        "Không đọc được dữ liệu phiếu lương. "
        "Đảm bảo module `tinh_luong` đã cài và DB đã có bảng `hr_phieu_luong`."
    )
    st.exception(exc)
