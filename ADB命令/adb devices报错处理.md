![adb����01](../picture/adb01.png)


	���ʹ��adb devices�����unknown host services
	������������룺netstat -ano|findstr "5037"
	�鿴���ĸ��˿�ռ����5037
	
![adb����02](../picture/adb02.png)

	����һ��
		�������������Ctrl+Shift+Esc
		�ڷ����е�PID�ҵ���ؽ��̺Ų����йرջ�ж��Ӧ��

	��������
		ʹ�����tasklist /fi ��pid eq 9212���鿴PID����
		
![adb����03](../picture/adb03.png)

��������taskkill /pid 9212 /f��ֹ����

![adb����04](../picture/adb04.png)

