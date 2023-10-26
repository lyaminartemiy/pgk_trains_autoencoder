from torchvision import transforms


train_transforms = transforms.Compose([
    transforms.ToTensor(),
    # transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    transforms.RandomHorizontalFlip(p=1),
    # transforms.RandomRotation(degrees=30),
    # transforms.ColorJitter(brightness=(0.1, 0.6), contrast=1, saturation=0, hue=0.4)
])

interference_transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
