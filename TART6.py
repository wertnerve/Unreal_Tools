# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TART6_UI_FINAL.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, 
    QListWidget, QLineEdit, QGraphicsView, QMenuBar, QMenu, QStatusBar, 
    QMainWindow, QSizePolicy, QTabWidget, QListWidgetItem
)
from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, 
    QPoint, QRect, QSize, QTime, QUrl, Qt
)
from PySide6.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, 
    QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, 
    QPalette, QPixmap, QRadialGradient, QTransform
)
from PySide6 import QtCore, QtGui, QtWidgets

import os
import unreal
from PIL import Image
from PIL.ImageQt import ImageQt  # Import ImageQt to convert PIL image to QPixmap
from io import BytesIO
import logging 
os.path.expanduser("~\\Documents")
def initialize_logger(print_to_screen = False):
    """
    Creates a logger

    Args:
        print_to_screen: for printing to screen as well as file
    """

    ###############
    # Basic Setup #
    ###############
    app_title = 'Tart6_Log_File'
    version_number = '1.0.0'
    # get the path the script was run from, storing with forward slashes
    source_path = os.path.dirname(os.path.realpath(__file__))
    # create a log filepath
    logfile_name = f'{app_title}.log'
    logfile = os.path.join(source_path, logfile_name)

    # tell the user where the log file is
    print(f'Logfile is {logfile}')

    # more initialization
    logger = logging.getLogger(f'{app_title} Logger')
    logger.setLevel(logging.INFO)
    
    ###############################
    # Formatter and Handler Setup #
    ###############################
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.INFO)
    # formatting information we want (time, logger name, version, etc.)
    formatter = logging.Formatter(f'%(asctime)s - %(name)s {version_number} - '
                                  '%(levelname)s - %(message)s')
    # setting the log file format
    file_handler.setFormatter(formatter)
    # clean up old handlers
    logger.handlers.clear()

    # add handler
    logger.addHandler(file_handler)

    # allowing to print to screen
    if print_to_screen:
        # create a new "stream handler" for logging/printing to screen
        console = logging.StreamHandler()
        logger.addHandler(console)
        # setting the print log format
        console.setFormatter(formatter)

    # return logger so it can be used
    return logger



def get_logger(print_to_screen = False):
    """
    Uses the logger.py module to create a logger

    Args:
        print_to_screen: for printing to screen as well as file
    """

    return logger.initialize_logger(print_to_screen)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 559)

        self.image_files = []
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 541))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.create_instances_button = QPushButton(self.tab)
        self.create_instances_button.setObjectName(u"create_instances_button")
        self.create_instances_button.setGeometry(QRect(390, 480, 271, 23))
        self.export_browse = QPushButton(self.tab)
        self.export_browse.setObjectName(u"export_browse")
        self.export_browse.setGeometry(QRect(690, 60, 91, 21))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 181, 16))
        self.material_browse = QPushButton(self.tab)
        self.material_browse.setObjectName(u"material_browse")
        self.material_browse.setGeometry(QRect(690, 30, 91, 21))
        self.asset_preview = QListWidget(self.tab)
        self.asset_preview.setObjectName(u"asset_preview")
        self.asset_preview.setGeometry(QRect(340, 130, 311, 251))
        self.folder_items_list = QtWidgets.QListWidget(self.tab)
        self.folder_items_list.setObjectName(u"folder_items_list")
        self.folder_items_list.setGeometry(QRect(10, 130, 241, 251))
        self.Asset_File_Label = QLabel(self.tab)
        self.Asset_File_Label.setObjectName(u"Asset_File_Label")
        self.Asset_File_Label.setGeometry(QRect(10, 0, 61, 20))
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 460, 47, 13))
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 460, 47, 13))
        self.prefix_edit = QLineEdit(self.tab)
        self.prefix_edit.setObjectName(u"prefix_edit")
        self.prefix_edit.setGeometry(QRect(100, 480, 113, 20))
        self.suffix_edit = QLineEdit(self.tab)
        self.suffix_edit.setObjectName(u"suffix_edit")
        self.suffix_edit.setGeometry(QRect(240, 480, 113, 20))
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 60, 71, 20))
        self.material_folder_label = QLabel(self.tab)
        self.material_folder_label.setObjectName(u"material_folder_label")
        self.material_folder_label.setGeometry(QRect(6, 30, 71, 20))
        self.export_folder = QLineEdit(self.tab)
        self.export_folder.setObjectName(u"export_folder")
        self.export_folder.setGeometry(QRect(100, 60, 561, 20))
        self.material_folder = QLineEdit(self.tab)
        self.material_folder.setObjectName(u"material_folder")
        self.material_folder.setGeometry(QRect(100, 30, 561, 20))
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(340, 110, 181, 16))
        self.asset_browse = QPushButton(self.tab)
        self.asset_browse.setObjectName(u"asset_browse")
        self.asset_browse.setGeometry(QRect(690, 0, 91, 21))
        self.asset_line = QLineEdit(self.tab)
        self.asset_line.setObjectName(u"asset_line")
        self.asset_line.setGeometry(QRect(100, 0, 561, 20))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.prefix_edit_2 = QLineEdit(self.tab_2)
        self.prefix_edit_2.setObjectName(u"prefix_edit_2")
        self.prefix_edit_2.setGeometry(QRect(70, 480, 113, 20))
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 460, 47, 13))
        self.png_browse = QPushButton(self.tab_2)
        self.png_browse.setObjectName(u"png_browse")
        self.png_browse.setGeometry(QRect(700, 30, 91, 21))
        self.png_preview_label = QLabel(self.tab_2)
        self.png_preview_label.setObjectName(u"png_preview_label")
        self.png_preview_label.setGeometry(QRect(350, 110, 181, 16))
       # self.asset_line_png_tab = QLineEdit(self.tab_2)
       # self.asset_line_png_tab.setObjectName(u"asset_line_png_tab")
       # self.asset_line_png_tab.setGeometry(QRect(100, 0, 571, 20))
        self.suffix_edit_2 = QLineEdit(self.tab_2)
        self.suffix_edit_2.setObjectName(u"suffix_edit_2")
        self.suffix_edit_2.setGeometry(QRect(220, 480, 113, 20))
        self.png_browser = QLineEdit(self.tab_2)
        self.png_browser.setObjectName(u"png_browser")
        self.png_browser.setGeometry(QRect(100, 30, 571, 20))
        self.png_image_preview = QLabel(self.tab_2)
        self.png_image_preview.setObjectName(u"png_image_preview")
        self.png_image_preview.setGeometry(QRect(350, 140, 351, 331))
        self.label = QLabel(self.tab_2)
      #  self.label.setObjectName(u"label")
      #  self.label.setGeometry(QRect(20, 0, 61, 20))
        self.asset_details_png_tab = QtWidgets.QListWidget(self.tab_2)
        self.asset_details_png_tab.setObjectName(u"asset_details_png_tab")
        self.asset_details_png_tab.setGeometry(QRect(5, 140, 261, 251))
        self.export_browse_png = QPushButton(self.tab_2)
        self.export_browse_png.setObjectName(u"export_browse_png")
        self.export_browse_png.setGeometry(QRect(700, 60, 91, 21))
       # self.asset_browse_pngtab = QPushButton(self.tab_2)
       # self.asset_browse_pngtab.setObjectName(u"asset_browse_pngtab")
       # self.asset_browse_pngtab.setGeometry(QRect(700, 0, 91, 21))
        self.png_browse_label = QLabel(self.tab_2)
        self.png_browse_label.setObjectName(u"png_browse_label")
        self.png_browse_label.setGeometry(QRect(0, 30, 71, 20))
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 60, 71, 20))
        self.export_folder_2 = QLineEdit(self.tab_2)
        self.export_folder_2.setObjectName(u"export_folder_2")
        self.export_folder_2.setGeometry(QRect(100, 60, 571, 20))
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(220, 460, 47, 13))
        self.asset_details_label_png_tab = QLabel(self.tab_2)
        self.asset_details_label_png_tab.setObjectName(u"asset_details_label_png_tab")
        self.asset_details_label_png_tab.setGeometry(QRect(20, 110, 181, 16))
        self.create_instances_button_2 = QPushButton(self.tab_2)
        self.create_instances_button_2.setObjectName(u"create_instances_button_2")
        self.create_instances_button_2.setGeometry(QRect(430, 490, 211, 23))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Batch Material Instance Generator", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.create_instances_button.setText(QCoreApplication.translate("MainWindow", u"Apply All Materials to Asset ", None))
        self.export_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Materials  In Folder Path (Total: 0)", None))
        self.material_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.Asset_File_Label.setText(QCoreApplication.translate("MainWindow", u"Static Mesh", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Prefix", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Suffix", None))
        self.prefix_edit.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.suffix_edit.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Export Folder:", None))
        self.material_folder_label.setText(QCoreApplication.translate("MainWindow", u"Material Path", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Asset Details", None))
        self.asset_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Apply Materials to Asset", None))
        self.prefix_edit_2.setText(QCoreApplication.translate("MainWindow", u"T_", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Prefix", None))
        self.png_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.png_preview_label.setText(QCoreApplication.translate("MainWindow", u"Selected Image Preview", None))
        self.suffix_edit_2.setText(QCoreApplication.translate("MainWindow", u"", None))
        #self.label.setText(QCoreApplication.translate("MainWindow", u"Static Mesh File", None))
        self.export_browse_png.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        #self.asset_browse_pngtab.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.png_browse_label.setText(QCoreApplication.translate("MainWindow", u"Image Folder", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Export Folder:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Suffix", None))
        self.asset_details_label_png_tab.setText(QCoreApplication.translate("MainWindow", u"Images in Folder", None))
        self.create_instances_button_2.setText(QCoreApplication.translate("MainWindow", u"Create and Export Textures", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Import Images as Textures", None))
    # retranslateUi


        #connect BATCH buttons to functions - TAB1
        self.asset_browse.clicked.connect(self.browse_asset_folder)
        self.material_browse.clicked.connect(self.browse_material_folder)
        self.export_browse.clicked.connect(self.browse_export_folder)
        self.create_instances_button.clicked.connect(self.create_instances)

        
        # Connect the PNG tab function to the button - TAB2
        self.png_browse.clicked.connect(self.browse_png_folder)
        self.create_instances_button_2.clicked.connect(self.import_png_and_create_texture)
        self.export_browse_png.clicked.connect(self.browse_export_folder_png_tab)
        self.asset_details_png_tab.itemClicked.connect(self.on_item_clicked)


    def create_material_from_texture(self, texture_path, material_name, destination_path):
    

            # Load the texture
        texture_asset = unreal.EditorAssetLibrary.load_asset(texture_path)
        if not texture_asset:
             unreal.log_error(f"Failed to load texture: {texture_path}")
             logger.info(f"Failed to load texture: {texture_path}")
             return None

    # Create a new material
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        material_asset = asset_tools.create_asset(material_name, destination_path, unreal.Material, unreal.MaterialFactoryNew())
    
        if not material_asset:
             unreal.log_error(f"Failed to create material: {material_name}")
             logger.info(f"Failed to create material: {material_name}")
             return None

    # Create a texture sample node
        texture_sample = unreal.MaterialEditingLibrary.create_material_expression(material_asset, unreal.MaterialExpressionTextureSample, -300, 0)
        texture_sample.texture = texture_asset

    # Connect texture sample to base color of material
        unreal.MaterialEditingLibrary.connect_material_property(texture_sample, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

    # Set material as two-sided (optional)
        material_asset.set_editor_property("two_sided", True)

    # Update the material
        unreal.MaterialEditingLibrary.recompile_material(material_asset)
        unreal.MaterialEditingLibrary.update_material_instance(material_asset)

    # Save the new material
        unreal.EditorAssetLibrary.save_loaded_asset(material_asset)

        return material_asset

    
    def import_png_and_create_texture(self):

        logger.info("Import PNG Function Called")
        destination_path = self.export_folder_2.text()
        logger.info(f"Destination Path: ",destination_path)
        destination_path = self.convert_to_unreal_path(destination_path)

        parts = destination_path.split("Unreal Projects")
    
         # If "Unreal Projects" is found in the path
        if len(parts) > 1:
        # Return the part after "Unreal Projects", removing leading slash or backslash
            destination_path = parts[1].lstrip('/\\')

        destination_path = destination_path.replace("/", "\\")
        logger.info(f"Destination path after convert to unreal path:",destination_path)
        
        png_file_path = self.png_browser.text().replace("/", "\\")
        logger.info("PNG File Path:",png_file_path)

        failures = 0
        failure_list = []
        file_paths = self.image_files
        logger.info("File paths:",file_paths)
        for file_name in file_paths:#os.listdir(png_file_path):
        
#            for file_path in file_paths:
             asset_name = file_name
            
        #copy asset to /game/ folder, keep it all local
             logger.info("Temp copying over asset to game folder")
             import shutil
             shutil.copy(asset_name, "/Game/")
             logger.info("Copied")
                  # Extract file name and extension
             base_name, extension = os.path.splitext(asset_name)
             asset_name = os.path.splitext(os.path.basename(file_name))[0]
             logger.info("Asset Name:", asset_name)


             

                # Construct custom texture name
             custom_name = f"{self.prefix_edit_2.text()}{asset_name}{self.suffix_edit_2.text()}"
             renamed_texture_path = f"/Game/{custom_name}{extension}"

             try:
                 os.rename("/Game/"+ asset_name + extension, renamed_texture_path)
                 logger.info("Renamed Asset name to ",renamed_texture_path)#asset_name + extension)
             except Exception as e:
                 logger.info("Unable to rename","/Game/"+ asset_name + extension,"to",renamed_texture_path)
                 logger.info(e)
                 failures += 1
                 failure_list.append(file_name)
             

             logger.info(f"Destination Path: ",destination_path)
             
            # Set up import task
             asset_path = renamed_texture_path#"/Game/"+asset_name+extension
             task = unreal.AssetImportTask()
             task.filename = asset_path
             task.destination_path = destination_path#destination_path
             task.replace_existing = True
             task.save = True
             task.automated = True

             
    
            # Execute the import task
             logger.info("Running task")
             unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

            
            # Get the imported texture asset
        
            # texture_asset_path = f"{destination_path}/{os.path.splitext(os.path.basename(png_file_path))[0]}"
             texture_asset_path = destination_path + "\\" + custom_name+extension
             texture_asset_path = texture_asset_path.replace("\\", "/")
        ###
             
             logger.info(f"Finding texture asset path:{texture_asset_path}")
             texture_asset = unreal.EditorAssetLibrary.find_asset_data(texture_asset_path).get_asset()
             
               
             if not texture_asset:
                #logger.info(f"Failed to import texture: {texture_asset_path}")
                pass
             else:
                 logger.info("found! Conversion complete on" + texture_asset_path)
            # return
        unreal.log("Completed texture conversion - texture assets located in: "+destination_path)
        logger.info("Completed texture conversion - texture assets located in: "+destination_path)

        if failures > 0:
            unreal.log("Total Failures:" + str(failures))
            logger.info("Total Failures:" + str(failures))
            for failure_path in failure_list:
                logger.info("FAILED FILE: "+failure_path)
        

    
    def format_asset_name(self, name):
    # Remove invalid characters and replace spaces with underscores
        invalid_chars = '/.:?'
        return ''.join(c if c not in invalid_chars else '_' for c in name).replace(' ', '_')


    def format_folder_path(self, path):
    # Ensure the path starts with /Game/ and doesn't contain invalid characters
          unreal.log("path before changes (format folder path function):")
          unreal.log(path)
          path = self.convert_to_unreal_path(path)
          if not path.startswith('/Game/'):
               path = '/Game/' + path.lstrip('/')
          unreal.log("Path after changes:")
          unreal.log(path)
          return '/'.join(self.format_asset_name(part) for part in path.split('/'))



    #QFileDialog.getExistingDirectory(None, "Select Export Folder")
    def get_all_files(self, directory):

        all_files = []
        unreal.log("Traversing "+directory)
        logger.info(f"Traversing {directory}")
        for root, _, files in os.walk(directory):
            logger.info(f"Root:{root} _:{_} Files{files}")
            for file in files:
                full_path = os.path.join(root, file)
                extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.jfif')
                file_name = str(file).lower()
              
               
                if file_name.endswith(extensions):
                    all_files.append(full_path)
        unreal.log("Traversed Directory, returning "+(str(len(all_files))) + " files")
        logger.info("Traversed Directory, returning "+(str(len(all_files))) + " files")
        self.image_files = all_files
        logger.info("IMAGE FILES:",self.image_files)
        return all_files
        

    def browse_png_folder(self):
        logger.info("Browse Png Folder Function Called")
        folder= QFileDialog.getExistingDirectory(None, "Select Image Folder For Texture Conversion") 
        #QFileDialog.getOpenFileName(None, "Select Image to convert to Material", "", "Image Files (*.png *.jpg *.bmp)")
        if folder:
            self.png_browser.setText(folder)
            

            filepath_list = self.get_all_files(folder)
             # Iterate over all files in the selected folder
            self.asset_details_png_tab.clear()

            self.asset_details_label_png_tab.setText(f"Items in Folder (Total: {len(filepath_list)})")
            for item in filepath_list:
                        self.asset_details_png_tab.addItem(item)
                        
            # Resize the image to fit within the asset_preview box
            if len(filepath_list) > 0:
                pixmap = QPixmap(filepath_list[0])
                scaled_pixmap = pixmap.scaled(self.png_image_preview.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                self.png_image_preview.setPixmap(scaled_pixmap)
                self.asset_details_png_tab.setCurrentItem(self.asset_details_png_tab.item(0))

    def on_item_clicked(self, item):
        file_path = item.text()
        pixmap = QPixmap(file_path)
        scaled_pixmap = pixmap.scaled(self.png_image_preview.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.png_image_preview.setPixmap(scaled_pixmap)


    def browse_export_folder_png_tab(self):
        folder = QFileDialog.getExistingDirectory(None, "Select Export Folder")
        if folder:
            self.export_folder_2.setText(folder)


    def browse_asset_folder(self):
        logger.info("Asset browse Function Function Called")
        filename, _ = QFileDialog.getOpenFileName(None, "Select Static Mesh Asset", "", )  # "Image Files (*.png *.jpg *.bmp)")
        if filename:
            self.asset_line.setText(filename)
            asset_path = self.asset_line.text().replace("\\", "/")
            asset_path = self.convert_to_unreal_path(asset_path)
            details = get_static_mesh_details(asset_path)
            self.asset_preview.clear()
            if details:
                for key, value in details.items():
                     item_text = f"{key}: {value}"
                     self.asset_preview.addItem(item_text)
            else :
                self.asset_preview.addItem("Invalid File Selected.")
                self.asset_preview.addItem("Asset is likely not a static mesh.")



    def browse_material_folder(self):
        logger.info("Browse Material Folder Called")

        folder = QFileDialog.getExistingDirectory(None, "Select Folder")
        if folder:
             self.material_folder.setText(folder)
             self.folder_items_list.clear()
        uasset_total = 0

        # Iterate over all files in the selected folder
        for item in os.listdir(folder):
               if item.endswith(".uasset"):
                # Build the full file path
                full_file_path = os.path.join(folder, item).replace("\\", "/")
                
                # Convert file path to asset path
                asset_path = self.convert_to_unreal_path(full_file_path)

                if asset_path:
                    # Load the asset from the path
                    asset = unreal.EditorAssetLibrary.load_asset(asset_path)
                    
                    # Check if the asset is a Material or MaterialInstance
                    if isinstance(asset, (unreal.Material, unreal.MaterialInstance)):
                        self.folder_items_list.addItem(item)
                        uasset_total += 1

        self.label_2.setText(f"Materials in Folder: (Total = {uasset_total})")



    def browse_export_folder(self):
        folder = QFileDialog.getExistingDirectory(None, "Select Folder")
        if folder:
            self.export_folder.setText(folder)




    
    def apply_material_to_asset(self, asset, material):
        log = str(f"Applying {material} to {asset}")
        unreal.log(log)
        logger.info(log)
    # Check if material is a string (path) or an object
        # Check if material is a string (path) or an object
        if isinstance(material, str):
            material_asset = unreal.EditorAssetLibrary.load_asset(material)
        else:
            material_asset = material

    # Check if asset is a string (path) or an object
        if isinstance(asset, str):
        # Convert the path to the correct Unreal Engine format
            #asset_path = self.convert_to_unreal_path(asset)
            asset_path = asset
            asset_object = unreal.EditorAssetLibrary.load_asset(asset_path)
        else:
            asset_object = asset

        if not material_asset:
             unreal.log_error(f"Failed to load material: {material}")
             logger.info(f"Failed to load material: {material}")
             return

        if not asset_object:
            unreal.log_error(f"Failed to load asset: {asset}")
            logger.info(f"Failed to load asset: {asset}")
            return

    # Check if the asset is a StaticMesh
        if isinstance(asset_object, unreal.StaticMesh):
        # Get the number of material slots
             unreal.log("asset object:")
             unreal.log(asset_object)
             num_materials = asset_object.get_num_sections(0)  # Assuming LOD 0

        # Apply the material to all slots
             for i in range(num_materials):
                asset_object.set_material(i, material_asset)

             unreal.log(f"Applied material {material_asset.get_name()} to {asset_object.get_name()}")
             logger.info(f"Applied material {material_asset.get_name()} to {asset_object.get_name()}")
        else:
             unreal.log_error(f"Asset {asset_object.get_name()} is not a StaticMesh")
             logger.info(f"Asset {asset_object.get_name()} is not a StaticMesh")

    # Save the modified asset
        unreal.EditorAssetLibrary.save_loaded_asset(asset_object)    
        logger.info(f"Saved {asset_object}")        



    def create_instances(self):
            
            logger.info("Create Instances Function Called")
            asset_path = self.asset_line.text().replace("\\", "/")
            material_folder = self.material_folder.text().replace("\\", "/")
            export_folder = self.export_folder.text().replace("\\", "/")

         # Convert to Unreal-relative paths and remove the .uasset extension
            asset_path = self.convert_to_unreal_path(asset_path)
            asset_name = os.path.splitext(os.path.basename(asset_path))[0]

    # Load all materials in the material folder
            for material_name in os.listdir(material_folder):
             material_path = os.path.join(material_folder, material_name).replace("\\", "/")
             material_path = self.convert_to_unreal_path(material_path)

             # Remove the .uasset extension
             material_name = os.path.splitext(os.path.basename(material_path))[0]
             material_path = os.path.join(os.path.dirname(material_path), material_name)

             try:
                material = unreal.EditorAssetLibrary.load_asset(material_path)
                unreal.log("Current Material: " + material_name)
                logger.info("Current Material: " + material_name)
             except:
                 unreal.log("Current file "+material_name+"Cannot be loaded, likely not a valid material")
                 logger.info("Current file "+material_name+"Cannot be loaded, likely not a valid material")
            # unreal.log(dir(material))
             if isinstance(material, unreal.Material):  # Check if it's a material
            # Create a new instance of the asset for each material
                unreal.log(material_name+ " is a Material instance")
                instance_name = f"{self.prefix_edit.text()}_{asset_name}_{material_name}_{self.suffix_edit.text()}"
                instance_path = os.path.join(export_folder, instance_name).replace("\\", "/")
                instance_path = self.convert_to_unreal_path(instance_path)

            # Duplicate the asset to create an instance
                unreal.EditorAssetLibrary.duplicate_asset(asset_path, instance_path)

            # Apply the material to the new asset instance
                self.apply_material_to_asset(instance_path, material)

                unreal.log("Material instance " + instance_name + " created successfully.")
                logger.info("Material instance " + instance_name + " created successfully.")

    
    def convert_to_unreal_path(self,path):
        logger.info(f"Converting {path} to unreal compatible path")
        unreal_project_dir = "/Game/"
        content_index = path.find("/Content/")
        if content_index != -1:
            relative_path = unreal_project_dir + path[content_index + len("/Content/"):]
            os.makedirs(os.path.dirname(relative_path), exist_ok=True)
            return os.path.splitext(relative_path)[0]  # Remove .uasset extension
        return path



def get_static_mesh_details(asset_path):
    static_mesh = unreal.load_asset(asset_path)
    unreal.log("Loaded Static Mesh:" + str(static_mesh))
    logger.info("Loaded Static Mesh:" + str(static_mesh))
    details = {}

    if isinstance(static_mesh, unreal.StaticMesh):
        details['Asset Name'] = static_mesh.get_name()
        details['Asset Path'] = asset_path
        details['Number of bounds'] = static_mesh.get_bounds()
        details['Current Material'] = static_mesh.get_material(0)
       
        
        # Asset metadata
        metadata = static_mesh.get_editor_property('asset_import_data')
        if metadata:
            details['Source File'] = metadata.get_first_filename()
            details['Source Data'] = str(metadata.get_editor_property('source_data'))
        #unreal.log(dir(metadata))
        #unreal.log(dir(metadata.get_editor_property('source_data')))
        # Lightmap resolution
        details['Lightmap Resolution'] = static_mesh.get_editor_property('light_map_resolution')
        
        # Nanite settings (if applicable)
        nanite_settings = static_mesh.get_editor_property('nanite_settings')
        if nanite_settings:
            details['Nanite Enabled'] = nanite_settings.get_editor_property('enabled')
        logger.info("All Static Mesh material Details extracted")
    else:
        unreal.log_error(f"Asset at {asset_path} is not a StaticMesh")
        return None

    return details

    

if __name__ == "__main__":
    import sys
    logger = initialize_logger(True)
    logger.info('Logger Initiated')
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
