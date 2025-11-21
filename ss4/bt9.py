from collections import namedtuple

Product = namedtuple("Product", ["id", "name", "quantity", "price"])
products = []


def add_product(products):
    product = Product(
        id=int(input("Nhập mã sản phẩm: ")),
        name=input("Nhập tên sản phẩm: "),
        quantity=int(input("Nhập số lượng sản phẩm: ")),
        price=float(input("Nhập giá sản phẩm: "))
    )
    products.append(product)
    print("Đã thêm sản phẩm:", product)


def show_products(products):
    if not products:
        print("Danh sách sản phẩm rỗng")
        return
    for product in products:
        print(product)


def find_product_index_by_id(products, id_):
    for idx, product in enumerate(products):
        if product.id == id_:
            return idx
    return -1


def search_product(products):
    id_ = int(input("Nhập mã sản phẩm: "))
    idx = find_product_index_by_id(products, id_)
    if idx == -1:
        print("Không tìm thấy sản phẩm")
    else:
        print(products[idx])


def update_product(products):
    id_ = int(input("Nhập mã sản phẩm cần cập nhật: "))
    idx = find_product_index_by_id(products, id_)
    if idx == -1:
        print("Không tìm thấy sản phẩm")
        return

    product = products[idx]
    print("Sản phẩm hiện tại:", product)

    new_name = input("Nhập tên mới (bỏ trống nếu giữ nguyên): ")
    new_quantity = input("Nhập số lượng mới (bỏ trống nếu giữ nguyên): ")
    new_price = input("Nhập giá mới (bỏ trống nếu giữ nguyên): ")

    new_product = Product(
        id=product.id,
        name=new_name if new_name else product.name,
        quantity=int(new_quantity) if new_quantity else product.quantity,
        price=float(new_price) if new_price else product.price
    )

    products[idx] = new_product
    print("Đã cập nhật:", new_product)


def delete_product(products):
    id_ = int(input("Nhập mã sản phẩm cần xóa: "))
    idx = find_product_index_by_id(products, id_)
    if idx == -1:
        print("Không tìm thấy sản phẩm")
    else:
        removed = products.pop(idx)
        print("Đã xóa:", removed)


def main():
    products = []
    choice = -1

    while choice != 0:
        print("Menu")
        print("1. Thêm sản phẩm mới")
        print("2. Hiển thị danh sách sản phẩm")
        print("3. Tìm kiếm sản phẩm theo mã sản phẩm")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm theo mã sản phẩm")
        print("0. Thoát")

        choice = int(input("Nhập lựa chọn: "))

        match choice:
            case 1:
                add_product(products)
            case 2:
                show_products(products)
            case 3:
                search_product(products)
            case 4:
                update_product(products)
            case 5:
                delete_product(products)
            case 0:
                print("Thoát chương trình")
            case _:
                print("Lựa chọn không hợp lệ")


main()
