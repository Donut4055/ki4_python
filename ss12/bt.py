
import json
import os
import matplotlib.pyplot as plt

# Constants
DATA_FILE = "data.json"

# Global variables
student_list = []


# ==================== CALCULATION FUNCTIONS ====================

def calculate_average_score(math, physics, chemistry):
    """
    Calculate the average score of three subjects.
    
    Args:
        math (float): Math score (0-10)
        physics (float): Physics score (0-10)
        chemistry (float): Chemistry score (0-10)
    
    Returns:
        float: Average score rounded to 2 decimal places
    """
    return round((math + physics + chemistry) / 3, 2)


def get_classification(avg_score):
    """
    Classify student performance based on average score.
    
    Args:
        avg_score (float): Average score (0-10)
    
    Returns:
        str: Classification in Vietnamese (Giỏi/Khá/Trung Bình/Yếu)
            - Giỏi (Excellent): >= 8.0
            - Khá (Good): >= 6.5
            - Trung Bình (Average): >= 5.0
            - Yếu (Weak): < 5.0
    """
    match avg_score:
        case score if score >= 8:
            return "Giỏi"
        case score if score >= 6.5:
            return "Khá"
        case score if score >= 5:
            return "Trung Bình"
        case _:
            return "Yếu"


# ==================== VALIDATION FUNCTIONS ====================

def validate_score(score):
    """
    Validate if a score is within the valid range (0-10).
    
    Args:
        score (str or float): Score to validate
    
    Returns:
        bool: True if score is valid (0-10), False otherwise
    """
    try:
        score = float(score)
        return 0 <= score <= 10
    except ValueError:
        return False


def validate_student_id(student_id, students):
    """
    Check if a student ID is unique (not already in the list).
    
    Args:
        student_id (str): Student ID to check
        students (list): List of student dictionaries
    
    Returns:
        bool: True if ID is unique, False if duplicate
    """
    for student in students:
        if student['student_id'] == student_id:
            return False
    return True


def find_student_by_id(student_id, students):
    """
    Find a student by their ID.
    
    Args:
        student_id (str): Student ID to search for
        students (list): List of student dictionaries
    
    Returns:
        dict or None: Student dictionary if found, None otherwise
    """
    for student in students:
        if student['student_id'] == student_id:
            return student
    return None


# ==================== FILE I/O FUNCTIONS ====================

def load_from_json():
    """
    Load student data from JSON file.
    
    Reads data from DATA_FILE and populates the global student_list.
    Creates an empty list if file doesn't exist or on error.
    
    Side Effects:
        - Modifies global student_list variable
        - Prints status messages to console
    """
    global student_list
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                student_list = json.load(f)
            print(f"✓ Đã tải {len(student_list)} sinh viên từ file {DATA_FILE}")
        except Exception as e:
            print(f"✗ Lỗi khi đọc file: {e}")
            student_list = []
    else:
        print(f"⚠ File {DATA_FILE} chưa tồn tại. Sẽ tạo mới khi lưu dữ liệu.")
        student_list = []


def save_to_json():
    """
    Save student data to JSON file.
    
    Writes the global student_list to DATA_FILE in UTF-8 encoding
    with pretty-printing (indent=2).
    
    Returns:
        bool: True if save successful, False otherwise
    
    Side Effects:
        - Writes to DATA_FILE
        - Prints status messages to console
    """
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(student_list, f, ensure_ascii=False, indent=2)
        print(f"✓ Đã lưu {len(student_list)} sinh viên vào file {DATA_FILE}")
        return True
    except Exception as e:
        print(f"✗ Lỗi khi ghi file: {e}")
        return False


# ==================== FEATURE 1: DISPLAY STUDENT LIST ====================

def display_student_list():
    """
    Display all students in a formatted table.
    
    Loads data from JSON file and displays:
    - STT (No.), Student ID, Name, Math, Physics, Chemistry, Average, Classification
    - Total student count
    
    Side Effects:
        - Calls load_from_json()
        - Prints formatted table to console
    """
    load_from_json()
    
    if not student_list:
        print("\n⚠ Danh sách sinh viên trống!")
        return
    
    print("\n" + "="*110)
    print(f"{'STT':<5} {'Mã SV':<10} {'Tên sinh viên':<25} {'Toán':<8} {'Lý':<8} {'Hóa':<8} {'ĐTB':<8} {'Xếp loại':<15}")
    print("="*110)
    
    for i, student in enumerate(student_list, 1):
        print(f"{i:<5} {student['student_id']:<10} {student['name']:<25} "
              f"{student['math_score']:<8.2f} {student['physics_score']:<8.2f} "
              f"{student['chemistry_score']:<8.2f} {student['avg_score']:<8.2f} "
              f"{student['classification']:<15}")
    
    print("="*110)
    print(f"Tổng số sinh viên: {len(student_list)}")


# ==================== FEATURE 2: ADD NEW STUDENT ====================

def add_student():
    """
    Add a new student to the list.
    
    Prompts user for:
    - Student ID (must be unique)
    - Name (cannot be empty)
    - Math, Physics, Chemistry scores (0-10)
    
    Auto-calculates average score and classification.
    
    Side Effects:
        - Modifies global student_list
        - Prints prompts and status messages to console
    """
    print("\n--- THÊM MỚI SINH VIÊN ---")
    
    # Input student ID with validation
    while True:
        student_id = input("Nhập mã sinh viên: ").strip()
        if not student_id:
            print("✗ Mã sinh viên không được để trống!")
            continue
        if not validate_student_id(student_id, student_list):
            print("✗ Mã sinh viên đã tồn tại!")
            continue
        break
    
    # Input name with validation
    name = input("Nhập tên sinh viên: ").strip()
    while not name:
        print("✗ Tên không được để trống!")
        name = input("Nhập tên sinh viên: ").strip()
    
    # Input math score with validation
    while True:
        math_score = input("Nhập điểm Toán (0-10): ").strip()
        if validate_score(math_score):
            math_score = float(math_score)
            break
        print("✗ Điểm không hợp lệ! Vui lòng nhập số từ 0-10.")
    
    # Input physics score with validation
    while True:
        physics_score = input("Nhập điểm Lý (0-10): ").strip()
        if validate_score(physics_score):
            physics_score = float(physics_score)
            break
        print("✗ Điểm không hợp lệ! Vui lòng nhập số từ 0-10.")
    
    # Input chemistry score with validation
    while True:
        chemistry_score = input("Nhập điểm Hóa (0-10): ").strip()
        if validate_score(chemistry_score):
            chemistry_score = float(chemistry_score)
            break
        print("✗ Điểm không hợp lệ! Vui lòng nhập số từ 0-10.")
    
    # Calculate average and classification
    avg_score = calculate_average_score(math_score, physics_score, chemistry_score)
    student_classification = get_classification(avg_score)
    
    # Create new student dictionary
    new_student = {
        'student_id': student_id,
        'name': name,
        'math_score': math_score,
        'physics_score': physics_score,
        'chemistry_score': chemistry_score,
        'avg_score': avg_score,
        'classification': student_classification
    }
    
    student_list.append(new_student)
    print(f"\n✓ Đã thêm sinh viên {name} (Mã: {student_id}) - ĐTB: {avg_score} - Xếp loại: {student_classification}")


# ==================== FEATURE 3: UPDATE STUDENT ====================

def update_student():
    """
    Update an existing student's information.
    
    Prompts for student ID, then allows updating individual scores.
    Press Enter to keep current value.
    Auto-recalculates average and classification after updates.
    
    Side Effects:
        - Modifies student data in global student_list
        - Prints prompts and status messages to console
    """
    print("\n--- CẬP NHẬT THÔNG TIN SINH VIÊN ---")
    
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip()
    student = find_student_by_id(student_id, student_list)
    
    if not student:
        print(f"✗ Không tìm thấy sinh viên có mã {student_id}")
        return
    
    print(f"\nThông tin hiện tại của sinh viên {student['name']}:")
    print(f"  Toán: {student['math_score']}, Lý: {student['physics_score']}, Hóa: {student['chemistry_score']}")
    print(f"  ĐTB: {student['avg_score']}, Xếp loại: {student['classification']}")
    
    print("\nNhập điểm mới (Enter để giữ nguyên):")
    
    # Update math score
    new_math = input(f"Điểm Toán [{student['math_score']}]: ").strip()
    if new_math:
        while not validate_score(new_math):
            print("✗ Điểm không hợp lệ!")
            new_math = input(f"Điểm Toán [{student['math_score']}]: ").strip()
        student['math_score'] = float(new_math)
    
    # Update physics score
    new_physics = input(f"Điểm Lý [{student['physics_score']}]: ").strip()
    if new_physics:
        while not validate_score(new_physics):
            print("✗ Điểm không hợp lệ!")
            new_physics = input(f"Điểm Lý [{student['physics_score']}]: ").strip()
        student['physics_score'] = float(new_physics)
    
    # Update chemistry score
    new_chemistry = input(f"Điểm Hóa [{student['chemistry_score']}]: ").strip()
    if new_chemistry:
        while not validate_score(new_chemistry):
            print("✗ Điểm không hợp lệ!")
            new_chemistry = input(f"Điểm Hóa [{student['chemistry_score']}]: ").strip()
        student['chemistry_score'] = float(new_chemistry)
    
    # Recalculate average and classification
    student['avg_score'] = calculate_average_score(
        student['math_score'], 
        student['physics_score'], 
        student['chemistry_score']
    )
    student['classification'] = get_classification(student['avg_score'])
    
    print(f"\n✓ Đã cập nhật thông tin sinh viên {student['name']}")
    print(f"  ĐTB mới: {student['avg_score']}, Xếp loại: {student['classification']}")


# ==================== FEATURE 4: DELETE STUDENT ====================

def delete_student():
    """
    Delete a student from the list.
    
    Prompts for student ID and requires confirmation before deletion.
    
    Side Effects:
        - Modifies global student_list (removes student)
        - Prints prompts and status messages to console
    """
    print("\n--- XÓA SINH VIÊN ---")
    
    student_id = input("Nhập mã sinh viên cần xóa: ").strip()
    student = find_student_by_id(student_id, student_list)
    
    if not student:
        print(f"✗ Không tìm thấy sinh viên có mã {student_id}")
        return
    
    print(f"\nSinh viên: {student['name']} (Mã: {student['student_id']})")
    confirmation = input("Bạn có chắc muốn xóa? (y/n): ").strip().lower()
    
    if confirmation == 'y':
        student_list.remove(student)
        print(f"✓ Đã xóa sinh viên {student['name']}")
    else:
        print("✗ Đã hủy thao tác xóa")


# ==================== FEATURE 5: SEARCH STUDENT ====================

def search_student():
    """
    Search for students by ID or name.
    
    Provides two search modes:
    1. By student ID (exact match)
    2. By name (partial match, case-insensitive)
    
    Displays results in a formatted table.
    
    Side Effects:
        - Prints prompts, search results, and status messages to console
    """
    print("\n--- TÌM KIẾM SINH VIÊN ---")
    print("1. Tìm theo mã sinh viên")
    print("2. Tìm theo tên sinh viên")
    
    choice = input("Chọn cách tìm kiếm (1/2): ").strip()
    
    match choice:
        case '1':
            student_id = input("Nhập mã sinh viên: ").strip()
            student = find_student_by_id(student_id, student_list)
            results = [student] if student else []
        case '2':
            search_name = input("Nhập tên sinh viên (có thể nhập một phần): ").strip().lower()
            results = [s for s in student_list if search_name in s['name'].lower()]
        case _:
            print("✗ Lựa chọn không hợp lệ!")
            return
    
    if not results:
        print("\n✗ Không tìm thấy sinh viên nào!")
        return
    
    print(f"\n✓ Tìm thấy {len(results)} sinh viên:")
    print("="*110)
    print(f"{'Mã SV':<10} {'Tên sinh viên':<25} {'Toán':<8} {'Lý':<8} {'Hóa':<8} {'ĐTB':<8} {'Xếp loại':<15}")
    print("="*110)
    
    for student in results:
        print(f"{student['student_id']:<10} {student['name']:<25} "
              f"{student['math_score']:<8.2f} {student['physics_score']:<8.2f} "
              f"{student['chemistry_score']:<8.2f} {student['avg_score']:<8.2f} "
              f"{student['classification']:<15}")
    print("="*110)


# ==================== FEATURE 6: SORT STUDENT LIST ====================

def sort_student_list():
    """
    Sort the student list by average score or name.
    
    Provides two sorting options:
    1. By average score (descending - highest first)
    2. By name (alphabetical A-Z)
    
    Displays the sorted list after sorting.
    
    Side Effects:
        - Modifies global student_list order
        - Calls display_student_list()
        - Prints prompts and status messages to console
    """
    print("\n--- SẮP XẾP DANH SÁCH SINH VIÊN ---")
    print("1. Sắp xếp theo điểm TB (giảm dần)")
    print("2. Sắp xếp theo tên (A-Z)")
    
    choice = input("Chọn cách sắp xếp (1/2): ").strip()
    
    match choice:
        case '1':
            student_list.sort(key=lambda x: x['avg_score'], reverse=True)
            print("✓ Đã sắp xếp theo điểm TB giảm dần")
        case '2':
            student_list.sort(key=lambda x: x['name'])
            print("✓ Đã sắp xếp theo tên A-Z")
        case _:
            print("✗ Lựa chọn không hợp lệ!")
            return
    
    display_student_list()


# ==================== FEATURE 7: STATISTICS ====================

def show_statistics():
    """
    Display statistics of students by classification.
    
    Counts and shows:
    - Number of students in each classification (Giỏi/Khá/Trung Bình/Yếu)
    - Percentage for each classification
    - Total student count
    
    Returns:
        dict or None: Dictionary with classification counts, or None if list is empty
    
    Side Effects:
        - Prints formatted statistics table to console
    """
    print("\n--- THỐNG KÊ ĐIỂM TRUNG BÌNH ---")
    
    if not student_list:
        print("⚠ Danh sách sinh viên trống!")
        return
    
    stats = {
        'Giỏi': 0,
        'Khá': 0,
        'Trung Bình': 0,
        'Yếu': 0
    }
    
    for student in student_list:
        stats[student['classification']] += 1
    
    print("\nKết quả thống kê:")
    print("="*50)
    print(f"{'Xếp loại':<20} {'Số lượng':<15} {'Tỷ lệ':<15}")
    print("="*50)
    
    total = len(student_list)
    for classification, count in stats.items():
        percentage = (count / total * 100) if total > 0 else 0
        print(f"{classification:<20} {count:<15} {percentage:.1f}%")
    
    print("="*50)
    print(f"{'Tổng cộng':<20} {total}")
    
    return stats


# ==================== FEATURE 8: DRAW CHART ====================

def draw_chart():
    """
    Draw a statistical chart of student classifications.
    
    Provides two chart types:
    1. Pie chart - Shows percentage distribution
    2. Bar chart - Shows count with labels
    
    Uses matplotlib for visualization with color-coded classifications:
    - Green (#2ecc71): Giỏi (Excellent)
    - Blue (#3498db): Khá (Good)
    - Orange (#f39c12): Trung Bình (Average)
    - Red (#e74c3c): Yếu (Weak)
    
    Side Effects:
        - Opens matplotlib window with chart
        - Prints prompts and status messages to console
    """
    print("\n--- VẼ BIỂU ĐỒ THỐNG KÊ ---")
    
    if not student_list:
        print("⚠ Danh sách sinh viên trống!")
        return
    
    # Gather statistics
    stats = {
        'Giỏi': 0,
        'Khá': 0,
        'Trung Bình': 0,
        'Yếu': 0
    }
    
    for student in student_list:
        stats[student['classification']] += 1
    
    print("1. Biểu đồ hình tròn (Pie Chart)")
    print("2. Biểu đồ cột (Bar Chart)")
    
    choice = input("Chọn loại biểu đồ (1/2): ").strip()
    
    labels = list(stats.keys())
    sizes = list(stats.values())
    colors = ['#2ecc71', '#3498db', '#f39c12', '#e74c3c']
    
    plt.figure(figsize=(10, 6))
    
    match choice:
        case '1':
            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            plt.title('Biểu đồ thống kê xếp loại học lực', fontsize=16, fontweight='bold')
            plt.axis('equal')
        case '2':
            plt.bar(labels, sizes, color=colors, edgecolor='black', linewidth=1.2)
            plt.xlabel('Xếp loại', fontsize=12, fontweight='bold')
            plt.ylabel('Số lượng sinh viên', fontsize=12, fontweight='bold')
            plt.title('Biểu đồ thống kê xếp loại học lực', fontsize=16, fontweight='bold')
            plt.grid(axis='y', alpha=0.3)
            
            # Add value labels on bars
            for i, v in enumerate(sizes):
                plt.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
        case _:
            print("✗ Lựa chọn không hợp lệ!")
            return
    
    plt.tight_layout()
    plt.show()
    print("✓ Đã hiển thị biểu đồ")


# ==================== FEATURE 9: SAVE TO FILE ====================

def save_data():
    """
    Save student data to JSON file.
    
    Wrapper function that calls save_to_json() and displays status.
    
    Side Effects:
        - Calls save_to_json()
        - Prints status messages to console
    """
    print("\n--- LƯU DỮ LIỆU ---")
    if save_to_json():
        print("✓ Dữ liệu đã được lưu thành công!")
    else:
        print("✗ Có lỗi khi lưu dữ liệu!")


# ==================== MENU FUNCTIONS ====================

def display_menu():
    """
    Display the main menu.
    
    Shows all 10 available features:
    1. Display student list
    2. Add new student
    3. Update student information
    4. Delete student
    5. Search student
    6. Sort student list
    7. Show statistics
    8. Draw chart
    9. Save to JSON file
    10. Exit
    
    Side Effects:
        - Prints formatted menu to console
    """
    print("\n" + "="*60)
    print("         CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("="*60)
    print("1.  Hiển thị danh sách sinh viên")
    print("2.  Thêm mới sinh viên")
    print("3.  Cập nhật thông tin sinh viên")
    print("4.  Xóa sinh viên")
    print("5.  Tìm kiếm sinh viên")
    print("6.  Sắp xếp danh sách sinh viên")
    print("7.  Thống kê điểm TB")
    print("8.  Vẽ biểu đồ thống kê điểm TB")
    print("9.  Lưu vào file JSON")
    print("10. Thoát")
    print("="*60)


def main():
    """
    Main program function.
    
    Entry point for the student management system.
    - Loads data from JSON file on startup
    - Displays menu and handles user input
    - Routes to appropriate functions based on user choice
    - Offers to save data before exit
    
    Side Effects:
        - Calls load_from_json() on startup
        - Runs infinite loop until user chooses to exit
        - May call save_to_json() on exit
        - Prints welcome message and prompts to console
    """
    print("\n🎓 CHÀO MỪNG ĐẾN VỚI CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN 🎓")
    
    # Load data on startup
    load_from_json()
    
    while True:
        display_menu()
        choice = input("\nNhập lựa chọn của bạn (1-10): ").strip()
        
        match choice:
            case '1':
                display_student_list()
            case '2':
                add_student()
            case '3':
                update_student()
            case '4':
                delete_student()
            case '5':
                search_student()
            case '6':
                sort_student_list()
            case '7':
                show_statistics()
            case '8':
                draw_chart()
            case '9':
                save_data()
            case '10':
                print("\n--- THOÁT CHƯƠNG TRÌNH ---")
                confirmation = input("Bạn có muốn lưu dữ liệu trước khi thoát? (y/n): ").strip().lower()
                if confirmation == 'y':
                    save_to_json()
                print("\n👋 Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
                break
            case _:
                print("\n✗ Lựa chọn không hợp lệ! Vui lòng chọn từ 1-10.")
        
        input("\nNhấn Enter để tiếp tục...")


main()
