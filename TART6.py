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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 559)
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
        self.asset_line_png_tab = QLineEdit(self.tab_2)
        self.asset_line_png_tab.setObjectName(u"asset_line_png_tab")
        self.asset_line_png_tab.setGeometry(QRect(100, 0, 571, 20))
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
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 61, 20))
        self.asset_details_png_tab = QtWidgets.QListWidget(self.tab_2)
        self.asset_details_png_tab.setObjectName(u"asset_details_png_tab")
        self.asset_details_png_tab.setGeometry(QRect(20, 140, 261, 251))
        self.export_browse_png = QPushButton(self.tab_2)
        self.export_browse_png.setObjectName(u"export_browse_png")
        self.export_browse_png.setGeometry(QRect(700, 60, 91, 21))
        self.asset_browse_pngtab = QPushButton(self.tab_2)
        self.asset_browse_pngtab.setObjectName(u"asset_browse_pngtab")
        self.asset_browse_pngtab.setGeometry(QRect(700, 0, 91, 21))
        self.png_browse_label = QLabel(self.tab_2)
        self.png_browse_label.setObjectName(u"png_browse_label")
        self.png_browse_label.setGeometry(QRect(20, 30, 71, 20))
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 60, 71, 20))
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
        self.prefix_edit_2.setText(QCoreApplication.translate("MainWindow", u"M_", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Prefix", None))
        self.png_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.png_preview_label.setText(QCoreApplication.translate("MainWindow", u"Selected Image Preview", None))
        self.suffix_edit_2.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Static Mesh File", None))
        self.export_browse_png.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.asset_browse_pngtab.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.png_browse_label.setText(QCoreApplication.translate("MainWindow", u"Image File", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Export Folder:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Suffix", None))
        self.asset_details_label_png_tab.setText(QCoreApplication.translate("MainWindow", u"Asset Details", None))
        self.create_instances_button_2.setText(QCoreApplication.translate("MainWindow", u"Apply Image to Asset (Create Material)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Convert Image to Material", None))
    # retranslateUi


        #connect BATCH buttons to functions - TAB1
        # Connect the asset browse button to the image picker
        self.asset_browse.clicked.connect(self.browse_asset_folder)
        # Connect the material browse button to the folder picker
        self.material_browse.clicked.connect(self.browse_material_folder)
        # Connect the Export Browse Button to the folder picker
        self.export_browse.clicked.connect(self.browse_export_folder)
        self.create_instances_button.clicked.connect(self.create_instances)

        
        # Connect the PNG tab function to the button - TAB2
        self.png_browse.clicked.connect(self.browse_png_folder)

        self.create_instances_button_2.clicked.connect(self.import_png_and_create_material)

        self.asset_browse_pngtab.clicked.connect(self.browse_asset_folder_png_tab)

        self.export_browse_png.clicked.connect(self.browse_export_folder_png_tab)



    def create_material_from_texture(self, texture_path, material_name, destination_path):
    

            # Load the texture
        texture_asset = unreal.EditorAssetLibrary.load_asset(texture_path)
        if not texture_asset:
             unreal.log_error(f"Failed to load texture: {texture_path}")
             return None

    # Create a new material
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        material_asset = asset_tools.create_asset(material_name, destination_path, unreal.Material, unreal.MaterialFactoryNew())
    
        if not material_asset:
             unreal.log_error(f"Failed to create material: {material_name}")
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

    
  
    def import_png_and_create_material(self):
        
        
        png_file_path = self.png_browser.text().replace("/", "\\")

        print("PNG File Path:",png_file_path)

        asset_name = self.asset_line_png_tab.text().replace("/", "\\")
        asset_path = asset_path = self.convert_to_unreal_path(self.asset_line_png_tab.text())
        #copy asset to /game/ folder, keep it all local
        print("Temp copying over asset  to game folder")
        import shutil
        shutil.copy(asset_name, "/Game/")
        print("Copied")

        asset_name = '//'+os.path.splitext(os.path.basename(asset_name))[0]
        print("Asset Name:", asset_name)
       # self.spawn_asset(asset_path)
            #if png file path is None, just copy the png to the export folder
        # Remove invalid characters from asset name
       # asset_name = self.format_asset_name(asset_name)
    
         # Ensure the destination path is valid
        
        destination_path = self.export_folder_2.text()
        print(f"Destination Path: ",destination_path)
        destination_path = self.convert_to_unreal_path(destination_path)

        parts = destination_path.split("Unreal Projects")
    
         # If "Unreal Projects" is found in the path
        if len(parts) > 1:
        # Return the part after "Unreal Projects", removing leading slash or backslash
            destination_path = parts[1].lstrip('/\\')

        destination_path = destination_path.replace("/", "\\")
        print(f"Destination path after convert to unreal path:",destination_path)
        # Set up import task
        task = unreal.AssetImportTask()
        task.filename = png_file_path
        task.destination_path = destination_path
        task.replace_existing = True
        task.save = True
        task.automated = True

        # Execute the import task
        unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

        # Get the imported texture asset
        
        texture_asset_path = f"{destination_path}/{os.path.splitext(os.path.basename(png_file_path))[0]}"
        texture_asset_path = texture_asset_path.replace("/", "\\")
        ###
        asset_path = self.asset_line_png_tab.text().replace("\\", "/")
        asset_path = self.convert_to_unreal_path(asset_path)
        
        print(f"Finding texture asset path:", texture_asset_path)
        texture_asset = unreal.EditorAssetLibrary.find_asset_data(texture_asset_path).get_asset()
        print("found")
        if not texture_asset:
            print(f"Failed to import texture: {texture_asset_path}")
            return

        
        
        # Create a new material
        print("Making new material")
        #material_name = f"M_{asset_name}"
        #material_asset = self.create_material_from_texture(texture_asset_path, material_name, destination_path)
        texture_asset = unreal.EditorAssetLibrary.load_asset(texture_asset_path)
        if not texture_asset:
            unreal.log_error(f"Failed to load texture: {texture_asset_path}")
            return
        
        print("Texture asset loaded")
        # Load the target asset (assuming it's a static mesh)
        print("Loading static mesh")
        target_asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        if not target_asset or not isinstance(target_asset, unreal.StaticMesh):
            unreal.log_error(f"Failed to load static mesh: {asset_path}")
            return

    # Create a new material instance
        print("Loading material instance")
        material_instance_factory = unreal.MaterialInstanceConstantFactoryNew()
        print("Loaded")
        material_instance_name = f"{self.prefix_edit_2.text()}_{unreal.Paths.get_base_filename(texture_asset_path)}_{self.suffix_edit_2.text()}"
        print("Loaded material instance name:", material_instance_name)
        material_instance_path = unreal.Paths.get_path(texture_asset_path)
        print("Loaded material instance path:", destination_path)
        material_instance = unreal.AssetToolsHelpers.get_asset_tools().create_asset(material_instance_name, '/Game/'+material_instance_path, unreal.MaterialInstanceConstant, material_instance_factory)

        # Set the texture parameter in the material instance
        print("Setting texture to material")
      #  unreal.MaterialEditingLibrary.set_material_instance_texture_parameter_value(material_instance, "Texture", texture_asset)
       # texture_sample = unreal.MaterialEditingLibrary.create_material_expression(texture_asset, unreal.MaterialExpressionTextureSample, -300, 0)
        #unreal.MaterialEditingLibrary.connect_material_property(texture_sample, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)
        #material_instance.set_editor_property("two_sided", True)

        instance_name = f"{self.prefix_edit.text()}_{asset_name}_{material_instance_name}_{self.suffix_edit.text()}"
        instance_path = os.path.join(destination_path, instance_name).replace("\\", "/")
        instance_path = self.convert_to_unreal_path(instance_path)

            # Duplicate the asset to create an instance
        unreal.EditorAssetLibrary.duplicate_asset(asset_path, instance_path)

        self.apply_material_to_asset(instance_path, material_instance)

        
    # Apply the material instance to the static mesh
      #  target_asset.set_material(0, material_instance)

        # Save the modified assets
       # unreal.EditorAssetLibrary.save_loaded_asset(target_asset)
       # unreal.EditorAssetLibrary.save_loaded_asset(material_instance)

        unreal.log(f"Applied texture {texture_asset_path} to {asset_path}")
        """
        material_factory = unreal.MaterialFactoryNew()
        material_asset = unreal.AssetToolsHelpers.get_asset_tools().create_asset(f"{asset_name}_Mat", destination_path, unreal.Material, material_factory)
        print("Material Asset created:",material_asset)
         # Create a texture sample node
        
        texture_sample = unreal.MaterialEditingLibrary.create_material_expression(material_asset, unreal.MaterialExpressionTextureSample, -300, 0)
        print("texture Sample created",texture_sample)
        print("TEXTURE SAMPLE DIR:",dir(texture_sample))
        texture_sample.texture = texture_asset
        
        # Connect texture sample to base color of material
        unreal.MaterialEditingLibrary.connect_material_property(texture_sample, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

        # Set material as two-sided
        material_asset.set_editor_property("two_sided", True)
        """
       # print(f"Material created: {material_asset.get_path_name()}")

        # Convert the asset path to Unreal Engine format
       # asset_path = self.convert_to_unreal_path(asset_name)
        #asset_path = asset_name.replace("\\", "/")
        #if asset_path:
         #   self.apply_material_to_asset(material_asset, asset_path)
        #else:
         #   print(f"Failed to convert asset path: {asset_path}")

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




    def browse_png_folder(self):

        filename, _ = QFileDialog.getOpenFileName(None, "Select Image to convert to Material", "", "Image Files (*.png *.jpg *.bmp)")
        if filename:
            self.png_browser.setText(filename)
            pixmap = QPixmap(filename)
            # Resize the image to fit within the asset_preview box
            scaled_pixmap = pixmap.scaled(self.png_image_preview.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.png_image_preview.setPixmap(scaled_pixmap)


    def browse_asset_folder_png_tab(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Select Static Mesh Asset", "", )  # "Image Files (*.png *.jpg *.bmp)")
        if filename:
            self.asset_line_png_tab.setText(filename)
            asset_path = self.asset_line_png_tab.text().replace("\\", "/")
            asset_path = self.convert_to_unreal_path(asset_path)
            details = get_static_mesh_details(asset_path)
            self.asset_details_png_tab.clear()
            if details:
                for key, value in details.items():
                     item_text = f"{key}: {value}"
                     self.asset_details_png_tab.addItem(item_text)

            else :
                self.asset_preview.addItem("Invalid File Selected.")
                self.asset_preview.addItem("Asset is likely not a static mesh.")

    def browse_export_folder_png_tab(self):
        folder = QFileDialog.getExistingDirectory(None, "Select Export Folder")
        if folder:
            self.export_folder_2.setText(folder)


    def browse_asset_folder(self):
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
        unreal.log("Applying")
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
             return

        if not asset_object:
            unreal.log_error(f"Failed to load asset: {asset}")
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
        else:
             unreal.log_error(f"Asset {asset_object.get_name()} is not a StaticMesh")

    # Save the modified asset
        unreal.EditorAssetLibrary.save_loaded_asset(asset_object)            


    
    def convert_to_unreal_path_png(self, path):
    # Convert a file system path to an Unreal Engine asset path
        content_index = path.lower().find("content")
        if content_index != -1:
            # Extract the part of the path after "Content"
            relative_path = path[content_index + 7:]  # +7 to skip "Content"
        # Replace backslashes with forward slashes
            relative_path = relative_path.replace("\\", "/")
            # Remove the file extension
            relative_path = os.path.splitext(relative_path)[0]
            # Add the "/Game/" prefix
            unreal_path = f"/Game{relative_path}"
            return unreal_path
        else:
             unreal.log_error(f"Invalid asset path: {path}")
             return None


    def create_instances(self):
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
             except:
                 unreal.log("Current file "+material_name+"Cannot be loaded, likely not a valid material")
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

    
    def convert_to_unreal_path(self,path):
        unreal_project_dir = "/Game/"
        content_index = path.find("/Content/")
        """
         if "/Content/" in path:
            import re
            pattern = r'.*?(/Content/.+\.uasset)'
            match = re.search(pattern, path)
            if match:
                return match.group(1)
            
        el"""
        if content_index != -1:
            relative_path = unreal_project_dir + path[content_index + len("/Content/"):]
            os.makedirs(os.path.dirname(relative_path), exist_ok=True)
            return os.path.splitext(relative_path)[0]  # Remove .uasset extension
        return path



def get_static_mesh_details(asset_path):
    static_mesh = unreal.load_asset(asset_path)
    unreal.log("Loaded Static Mesh:" + str(static_mesh))
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
        unreal.log(dir(metadata))
        unreal.log(dir(metadata.get_editor_property('source_data')))
        # Lightmap resolution
        details['Lightmap Resolution'] = static_mesh.get_editor_property('light_map_resolution')
        
        # Nanite settings (if applicable)
        nanite_settings = static_mesh.get_editor_property('nanite_settings')
        if nanite_settings:
            details['Nanite Enabled'] = nanite_settings.get_editor_property('enabled')
        print("All Static Mesh material Details extracted")
    else:
        unreal.log_error(f"Asset at {asset_path} is not a StaticMesh")
        return None

    return details

    

if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
