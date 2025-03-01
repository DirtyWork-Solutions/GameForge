import json
import yaml
import csv
import xml.etree.ElementTree as ET

from pyutile.reporting.logged import log as logger


def read_json(file_path):
    """Read data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logger.info(f"Successfully read JSON file: {file_path}")
            return data
    except Exception as e:
        logger.error(f"Error reading JSON file: {file_path} - {e}")
        raise


def write_json(data, file_path):
    """Write data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logger.info(f"Successfully wrote JSON file: {file_path}")
    except Exception as e:
        logger.error(f"Error writing JSON file: {file_path} - {e}")
        raise


def read_yaml(file_path):
    """Read data from a YAML file."""
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            logger.info(f"Successfully read YAML file: {file_path}")
            return data
    except Exception as e:
        logger.error(f"Error reading YAML file: {file_path} - {e}")
        raise


def write_yaml(data, file_path):
    """Write data to a YAML file."""
    try:
        with open(file_path, 'w') as file:
            yaml.safe_dump(data, file)
            logger.info(f"Successfully wrote YAML file: {file_path}")
    except Exception as e:
        logger.error(f"Error writing YAML file: {file_path} - {e}")
        raise


def read_csv(file_path):
    """Read data from a CSV file."""
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            logger.info(f"Successfully read CSV file: {file_path}")
            return data
    except Exception as e:
        logger.error(f"Error reading CSV file: {file_path} - {e}")
        raise


def write_csv(data, file_path):
    """Write data to a CSV file."""
    try:
        with open(file_path, 'w', newline='') as file:
            if data:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
                logger.info(f"Successfully wrote CSV file: {file_path}")
    except Exception as e:
        logger.error(f"Error writing CSV file: {file_path} - {e}")
        raise


def read_xml(file_path):
    """Read data from an XML file."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = [{child.tag: child.text for child in elem} for elem in root]
        logger.info(f"Successfully read XML file: {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error reading XML file: {file_path} - {e}")
        raise


def write_xml(data, file_path):
    """Write data to an XML file."""
    try:
        root = ET.Element("root")
        for item in data:
            elem = ET.Element("item")
            for key, value in item.items():
                child = ET.Element(key)
                child.text = str(value)
                elem.append(child)
            root.append(elem)
        tree = ET.ElementTree(root)
        tree.write(file_path)
        logger.info(f"Successfully wrote XML file: {file_path}")
    except Exception as e:
        logger.error(f"Error writing XML file: {file_path} - {e}")
        raise


def load_data(file_path):
    """Load data from a file, determining the format based on the file extension."""
    if file_path.endswith('.json'):
        return read_json(file_path)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        return read_yaml(file_path)
    elif file_path.endswith('.csv'):
        return read_csv(file_path)
    elif file_path.endswith('.xml'):
        return read_xml(file_path)
    else:
        raise ValueError("Unsupported file format")


def save_data(data, file_path):
    """Save data to a file, determining the format based on the file extension."""
    if file_path.endswith('.json'):
        write_json(data, file_path)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        write_yaml(data, file_path)
    elif file_path.endswith('.csv'):
        write_csv(data, file_path)
    elif file_path.endswith('.xml'):
        write_xml(data, file_path)
    else:
        raise ValueError("Unsupported file format")
